import os
from time import sleep, time

from evdev import InputDevice, ecodes, ff, list_devices

"""
==============================================================================
Project:     Universal Constant-Force Spring Emulator
Author:      Stan Swanborn
Description: This script provides a software-based "Spring" effect for Force
             Feedback (FFB) steering wheels on Linux. It is specifically
             designed for Direct Drive (DD) wheelbases that may lack native
             FF_SPRING support.

Functionality:
    1. Auto-detects the first available Force Feedback device.
        1.1 Manual override for input event available.
    2. Monitors the wheel's ABS_X axis position.
    3. Calculates a reactive centering force using a configurable Root-Curve.
    4. Updates the FF_CONSTANT effect at high frequency (up to 1000Hz).

Usage:
    Run WITHOUT sudo/root privileges, it is able to see any input device
        evtest would be able to see. If it cannot find your device, make a
        custom udev rule allowing access on the user level.

    Adjust MAX_FORCE_PERCENT and POWER_FACTOR to tune the feel.
==============================================================================
"""

# ================== CONFIG ==================
DEVICE_PATH = None  # When set to None, we will find the first Force Feedback device. Override here if necessary with correct /dev/input/eventXX
MIN_UPDATE_INTERVAL = 0.001  # 1ms (1000Hz) - Max precision for DD
# FORCE SETTINGS
MAX_FORCE_PERCENT = 10.0
# POWER_FACTOR (Sensitivity):
# 1.0 = Linear
# 0.5 = Square Root (Very sensitive at center, zero at zero)
# 0.7 = Good middle ground for "quick pick up"
POWER_FACTOR = 0.65
# ===========================================


def find_ff_device():
    """Finds the first device that supports Force Feedback."""
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
        # Check if EV_FF (Force Feedback) is in the device's capabilities
        if ecodes.EV_FF in device.capabilities():
            return device
    return None


def percent_to_level(percent: float) -> int:
    """Convert 0-100% to unsigned magnitude (0-32767)"""
    return int((max(0, min(100, percent)) / 100.0) * 32767)


# --- DEVICE INITIALIZATION ---
ff_device = None

if DEVICE_PATH:
    try:
        ff_device = InputDevice(DEVICE_PATH)
    except Exception as e:
        print(f"❌ Error: Could not open specified device {DEVICE_PATH}: {e}")
else:
    print("🔍 Searching for Force Feedback devices...")
    ff_device = find_ff_device()

if not ff_device:
    print("❌ Error: No Force Feedback device found!")
    exit(1)

print(f"✅ Using Device: {ff_device.name} ({ff_device.path})")

# --- CALIBRATION ---
# Use .absinfo() to get the actual min/max/fuzz/flat data for the axis
abs_info = ff_device.absinfo(ecodes.ABS_X)
if abs_info:
    CENTER = (abs_info.max + abs_info.min) / 2
    print(f"✅ Calibrated Center: {CENTER} (Range: {abs_info.min} - {abs_info.max})")
else:
    CENTER = 32768
    print("⚠️ Could not detect axis range, using fallback.")


os.set_blocking(ff_device.fd, False)

# 1. PRE-CREATE THE EFFECT OBJECT
constant_eff = ff.Constant(level=0, envelope=ff.Envelope(0, 0, 0, 0))
effect = ff.Effect(
    ecodes.FF_CONSTANT,
    -1,
    0,
    ff.Trigger(0, 0),
    ff.Replay(0, 0),
    ff.EffectType(ff_constant_effect=constant_eff),
)

# 2. INITIAL UPLOAD AND START
eff_id = ff_device.upload_effect(effect)
effect.id = eff_id
ff_device.write(ecodes.EV_FF, eff_id, 1)

print(f"✅ Root-Curve Spring Active on {ff_device.name}")
print(f"🚀 Sensitivity: {POWER_FACTOR} (Lower is more sensitive at center)")

last_update = 0
last_level = 0

try:
    while True:
        try:
            for event in ff_device.read():
                if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X:
                    now = time()
                    if now - last_update < MIN_UPDATE_INTERVAL:
                        continue

                    # Calculate deviation
                    deviation = event.value - CENTER

                    if deviation == 0:
                        level = 0
                    else:
                        normalized_dev = abs(deviation) / CENTER

                        # ROOT CALCULATION:
                        # Power < 1.0 makes the curve steep at the start but keeps 0 at 0.
                        target_pct = MAX_FORCE_PERCENT * (normalized_dev**POWER_FACTOR)
                        magnitude = percent_to_level(target_pct)

                        # DIRECTIONAL LOGIC (PERSISTED):
                        # Deviation > 0 (Left) -> Negative Force (Pull Right)
                        # Deviation < 0 (Right) -> Positive Force (Pull Left)
                        if deviation > 0:
                            level = magnitude
                        else:
                            level = -magnitude

                    # 3. UPDATE IN-PLACE
                    if level != last_level:
                        effect.u.ff_constant_effect.level = level
                        ff_device.upload_effect(effect)
                        last_level = level
                        last_update = now

        except BlockingIOError:
            pass

        # Reduced sleep for 1000Hz potential
        sleep(0.0001)

except KeyboardInterrupt:
    print("\nStopping...")
finally:
    if "ff_device" in locals():
        try:
            ff_device.write(ecodes.EV_FF, effect.id, 0)
            ff_device.erase_effect(effect.id)
            ff_device.close()
            print("Cleaned up.")
        except:
            pass
