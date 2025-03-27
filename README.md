# Linux steering wheels FFB support

## Ranks

Ranks are based on user testing and results may vary due to differences in the hardware.

### Platinum

Works fully with the recommended driver with extensive testing. Most common FFB effects implemented.

### Gold

Works fully but it's less tested and there might be some minor issues. Most common FFB effects implemented.

### Silver

Works almost fully. Some FFB effects might be missing or some other significant issues which might be
important in some cases. Workarounds might be available.

### Bronze

Major bugs or missing FFB effects which limit its use. It might be enough in some cases
but it's far from fully working.

### Broken

The device might be recognized as a gamepad/joystick but there's no FFB.

### (empty)

Device not tested at all. May be working, may be not. Contributions welcome!

## Table of compatibility

Read also related sections for each driver below for more information.

| Manufacturer | Device names         | VID  | PID  | Support  | Driver        | Proton compatibility |
|--------------|----------------------|------|------|----------|-----------------|--------------|
| Asetek       | Invicta              | 2433 | f300 | Gold[^13] | hid-universal-pidff[^1] | Works |
| Asetek       | Forte                | 2433 | f301 | Gold[^13] | hid-universal-pidff[^1] | Works |
| Asetek       | La Prima             | 2433 | f303 | Gold[^13] | hid-universal-pidff[^1] | Works |
| Asetek       | Tony Kannan          | 2433 | f306 | Gold[^13] | hid-universal-pidff[^1] | Works |
| Cammus       | C5                   | 3416 | 0301 | Platinum | hid-universal-pidff[^1] | Works[^10] |
| Cammus       | C12                  | 3416 | 0302 | Platinum | hid-universal-pidff[^1] | Works[^10] |
| Fanatec      | CSL Elite            | 0eb7 | 0e03 | Gold     | hid-fanatecff[^7] | |
| Fanatec      | CSL Elite (PS4)      | 0eb7 | 0005 | Gold     | hid-fanatecff[^7] | |
| Fanatec      | DD                   | 0eb7 | 0020 | Gold     | hid-fanatecff[^7] | |
| Fanatec      | DD Pro               | 0eb7 | 0020 | Gold     | hid-fanatecff[^7] | |
| Fanatec      | Clubsport DD         | 0eb7 | 0020 | Gold     | hid-fanatecff[^7] | |
| Fanatec      | ClubSport Wheel Base V2 |0eb7 | 0001 | Silver | hid-fanatecff[^7] | |
| Fanatec      | ClubSport Wheel Base V2.5 | 0eb7 |0004 | Silver | hid-fanatecff[^7] | |
| Fanatec      | Podium DD1           | 0eb7 | 0006 | Silver   | hid-fanatecff[^7] | |
| Fanatec      | Podium DD2           | 0eb7 | 0007 | Silver   | hid-fanatecff[^7] | |
| Fanatec      | CSR Elite            | 0eb7 | 0011 | Silver   | hid-fanatecff[^7] | |
| FFBeast      | Wheel                | 045b | 59d7 | Platinum | hid-universal-pidff[^1]  | Works |
| Logitech     | MOMO Wheel           | 046d | c295 | Platinum | hid-logitech[^2] | Works |
| Logitech     | DFP                  | 046d | c298 | Platinum | hid-logitech[^2] | Works |
| Logitech     | DFGT                 | 046d | c29a | Platinum | hid-logitech[^2] | Works |
| Logitech     | G25                  | 046d | c29b | Platinum | hid-logitech[^2] | Works |
| Logitech     | G27                  | 046d | c29b | Platinum | hid-logitech[^2] | Works |
| Logitech     | G29                  | 046d | c24f | Platinum | hid-logitech[^2] | Works |
| Logitech     | G920                 | 046d | c262 | Silver   | hid-logitech-hidpp[^8] | Works |
| Logitech     | G923 (Xbox edition)  | 046d | c26d | Silver   | hid-logitech-hidpp[^8] | Works |
| Logitech     | G923 (PS edition)    | 046d | c267 | Platinum | hid-logitech[^3] | Works |
| Logitech     | G Pro                | 046d | c272 | Bronze   | hid-logitech-hidpp[^4] | Works[^10] |
| Moza         | R3                   | 346e | 0005 | Platinum | hid-universal-pidff[^1] | Works |
| Moza         | R5                   | 346e | 0004 | Platinum | hid-universal-pidff[^1] | Works |
| Moza         | R9  (v1/v2/v3)       | 346e | 0002 | Platinum | hid-universal-pidff[^1] | Works |
| Moza         | R12 (v1/v2)          | 346e | 0006 | Platinum | hid-universal-pidff[^1] | Works |
| Moza         | R16 (v1/v2)          | 346e | 0000 | Platinum | hid-universal-pidff[^1] | Works |
| Moza         | R21 (v1/v2)          | 346e | 0000 | Platinum | hid-universal-pidff[^1] | Works |
| OpenFFBoard  |                      | 1209 | ffb0 | Platinum | hid-pidff[^1] | Works |
| PXN          | V10                  | 11ff | 3245 | Gold     | hid-universal-pidff[^1] | Works |
| PXN          | V12                  | 11ff | 1212 | Gold     | hid-universal-pidff[^1] | Works |
| PXN          | V12 Lite             | 11ff | 1112 | Gold     | hid-universal-pidff[^1] | Works |
| PXN          | V12 Lite (SE?)       | 11ff | 1211 | Gold     | hid-universal-pidff[^1] | Works |
| Lite Star    | GT987 FF	      | 11ff | 2141 | Gold     | hid-universal-pidff[^1] | Works |
| Simagic      | M10                  | 0483 | 0522 | Silver   | hid-pidff[^5] | Works  |
| Simagic      | Alpha Mini           | 0483 | 0522 | Silver/Broken[^6] :warning: | hid-pidff[^5] | Works |
| Simagic      | Alpha                | 0483 | 0522 | Silver/Broken[^6] :warning: | hid-pidff[^5] | Works |
| Simagic      | Alpha Ultimate       | 0483 | 0522 | Silver/Broken[^6] :warning: | hid-pidff[^5] | Works |
| Simucube     | Simucube 1           | 16d0 | 0d5a | Silver   | hid-pidff[^1] | Works[^11] |
| Simucube     | Simucube 2 Sport     | 16d0 | 0d61 | Silver   | hid-pidff[^1] | Works[^11] |
| Simucube     | Simucube 2 Pro       | 16d0 | 0d60 | Silver   | hid-pidff[^1] | Works[^11] |
| Simucube     | Simucube 2 Ultimate  | 16d0 | 0d5f | Silver   | hid-pidff[^1] | Works[^11] |
| SimXperience | AccuForce Pro        | 1fc9 | 804c | Platinum | hid-pidff[^1] |  |
| Thrustmaster | Nascar Pro FF2       | 044f | b605 |          | hid-tmff | |
| Thrustmaster | FGT Rumble Force     | 044f | b651 |          | hid-tmff | |
| Thrustmaster | RGT FF CLUTCH        | 044f | b653 |          | hid-tmff | |
| Thrustmaster | FGT Force Feedback   | 044f | b654 |          | hid-tmff | |
| Thrustmaster | F430 Force Feedback  | 044f | b65a |          | hid-tmff | |
| Thrustmaster | T248                 | 044f | b696 | Gold     | hid-tmff2[^9] | |
| Thrustmaster | T300RS (PS3 mode)    | 044f | b66e | Gold     | hid-tmff2[^9] | |
| Thrustmaster |T300RS (PS3 advanced mode)|044f|b66f| Gold     | hid-tmff2[^9] | |
| Thrustmaster | T300RS (PS4 mode)    | 044f | b66d | Gold     | hid-tmff2[^9] | |
| Thrustmaster | TX                   | 044f | b669 | Gold     | hid-tmff2[^9] | |
| Thrustmaster | TS-XV                | 044f |      | Gold     | hid-tmff2[^9] | |
| Turtle Beach |                      |      |      |          | | |
| VRS          | DirectForce Pro      | 0483 | a355 | Platinum[^14] | hid-universal-pidff[^1] | Works |

[^1]: Full native support since Linux 6.15. Plug and play
[^2]: Default driver lacks most effects. Use [patched driver](https://github.com/berarma/new-lg4ff).
[^3]: Not supported by default driver. Use [patched driver](https://github.com/berarma/new-lg4ff).
[^3]: Not supported by default driver. Use [patched driver](https://github.com/JacKeTUs/hid-logitech-hidpp).
[^5]: HID PID with caveats. Use [patched driver](https://github.com/JacKeTUs/simagic-ff).
[^6]: Only works with firmware versions up to v159.
[^7]: Custom module [hid-fanatecff](https://github.com/gotzl/hid-fanatecff)
[^8]: Full USB command queue errors. Using [ffbwrap]() can help in some situations.
[^9]: Custom module [hid-tmff2](https://github.com/Kimplul/hid-tmff2).
[^10]: See section on [joystick detection](#joystick-detection).
[^11]: Read [here about how to setup Simucube base](https://granitedevices.com/wiki/Using_Simucube_wheel_base_in_Linux).
And a [Success case](https://community.granitedevices.com/t/simucube-2-discussion-thread/2664/1606).
[^12]: Only Wheel mode was tested by user.
[^13]: You need to enable "high torque mode" after device is turned on/plugged in.
More info here: [asetek_wheelbase_cli](https://github.com/moonrail/asetek_wheelbase_cli)
[^14]: Some VRS DirectForce Pro units have a "power saving" feature which disables force feedback up until the
wheel is moved a little. doesn't hurt it's normal performance.

## hid-pidff

The kernel module `hid-pidff` implements the [HID PID specification](https://www.usb.org/sites/default/files/documents/pid1_01.pdf).
HID PID is a standard for USB devices which includes FFB. Although this standard is several years old, most older and
low end wheels don't implement it, but most high and some middle end wheels do.

With Linux 6.15, the generic `hid-pidff` driver was upgraded and made more compatible with wide range of devices out of
the box. Some devies still need some fixes like fixed direction for Moza deivces (caused by a bug in SDL which was
[fixed](https://github.com/libsdl-org/SDL/pull/12031)), permissive device dontrol field search for VRS. More
importantly, Moza, Camus and others define more than 80 buttons which is a current Linux
limitation for joysticks and gamepads.

Linux 6.15 introduces `hid-universal-pidff`, an extension to the generic PID driver, which extends usable button range,
sets better default fuzz/flat values and can be made to fix device descriptors if needed. Additionally, it enables us
to provide an initial set of newly-introduced pidff quirks.

### Duration issue

> [!NOTE]
> Fixed in Linux 6.15

The driver doesn't play any FFB effect out of the box due to a flaw in its API.

Although undocumented, Linux drivers and applications (including Wine) have always used value 0x0 for an infinite effect
length, but the hid-pidff driver uses value 0xFFFF instead. When an effect with length 0x0 is uploaded, it plays no
effect. The HID PID specification defines an infinite length effect with value 0xFFFF but this specification is for the
hardware and isn't tied to Linux in any way.

To work around the issue without custom drivers you could use [ffbwrap](https://github.com/berarma/ffbtools) tool.
For example, launch games with command:

```shell
ffbwrap --duration-fix /dev/input/by-id/usb-Your-Wheel-event-joystick %command%
```

### `a7` descriptor issue

> [!NOTE]
> Fixed in Linux 6.15

Descriptor `0xa7` (effect delay) is not required for Windows HID PID implementation. Some manufacturers (including
Simucube at first, later Simagic and Cammus) didn't implement that parameter in their firmware. But in Linux HID PID
implementation `0xa7` descriptor is mandatory, and device without it can't be initialized with hid-pidff driver.
Simucube [fixed it in latest firmware (1.0.49)](https://granitedevices.com/wiki/SimuCUBE_firmware_releases).

Some devices will require a patched hid-pidff driver which removes `0xa7` descriptor requirement and enables FFB.

## hid-logitech-hidpp

This module implements HID++, Logitech's own specification for FFB. It's used in wheel models compatible with XBox.
This models do almost everything in hardware, while models using hid-logitech need assistance from the driver.

### Queue full errors

In some games, when using this driver the FFB can lag behind so much that it's unbearable.

This driver sends commands to the wheel at the same rate they're sent by the game. When the game is sending FFB commands
at a very fast rate the command queue fills and a warning message appears in dmesg about the full queue. As a
consequence the FFB starts lagging behind and looses some FFB commands.

In some games, the rate at which the FFB commands are sent is tied to the frame rate, thus it may work well at lower
frame rates but fill the queue at higher frame rates.

Some games allow to configure the rate at which FFB commands are sent. Lowering that value can help and even
fix the issue.

[ffbwrap](https://github.com/berarma/ffbtools) can be used to work around it when the application can't be configured
to send commands at a lower rate. Needs testing.

## SDL

SDL tries to heuristically guess which devices are gamepads and ignores everything that doesn't look like one. This
means wheels and pedals might be ignored by SDL. This has been partially fixed by adding a
[whitelist](https://github.com/libsdl-org/SDL/blob/main/src/joystick/SDL_joystick.c#L340) of wheels. This list has
to be updated continuously with new models being tested.

Recent updates to SDL created SDL Hint variable to dynamically extend wheel devices list[^15]. You need to just
export `SDL_JOYSTICK_WHEEL_DEVICES=0x<VID>/0x<PID>,0x<VID2>/0x<PID2>` before you launching something.

## Wine/Proton caveats

### Joystick detection

Even if the device is ranked well, there may be some small issues regarding SDL wheel detection in Steam.

Also, for devices not present in whitelist, Steam uses sandboxed SDL1.2 to detect devices.
It has one small rule to detect all kinds of joysticks, function
[EV_IsJoystick()](https://github.com/libsdl-org/SDL-1.2/blob/main/src/joystick/linux/SDL_sysjoystick.c#L382-L398).
And basically, for the device to be classed as a joystick, it must have either X and Y axes or a X and Y hat, and
must have a trigger, A button, or 1 button. On some devices Y axis not exists (Logitech G Pro), and therefore, for SDL,
that device is not a joystick and no need to forward it to the game. Native apps will work perfectly, Wine apps too,
but not Steam+Proton games. We could fix it by changing descriptor axis, something like rename Rz to Y, and wheel
will work in Proton now

The environment variable `SDL_JOYSTICK_WHEEL_DEVICES` can be used to fix it.

Alternatively, [Boxflat](https://github.com/Lawstorant/boxflat) has "Detection fix" functionality.

[Link to the Proton issue](https://github.com/ValveSoftware/Proton/issues/5126)

## Steam settings for ~all devices and ~all games

1. Turn Steam Input off in game settings
2. Use recent Proton version for non-native games. 7 version known for having issues with HID devices detection.
3. If game does not detect your device, try [setting SDL Hint](https://github.com/libsdl-org/SDL/issues/8595)
   environment variable in game launch command like so:

    ```
    SDL_JOYSTICK_WHEEL_DEVICES=0x<VID>/0x<PID> %command%
    ```
    This is only relevant for devices which are, for various reasons, not in a SDL whitelist[^14] (yet), or for
    older Steam runtime versions which does not have updated SDL library.

4. If none of that worked, create an issue, where members of the community will try to help you with your specific game

## Links

- [Logitech FFb Protocol v1.6](https://opensource.logitech.com/wiki/force_feedback/Logitech_Force_Feedback_Protocol_V1.6.pdf).
- [hid-logitech-hidpp kernel module](https://elixir.bootlin.com/linux/latest/source/drivers/hid/hid-logitech-hidpp.c).
- [hid-pidff kernel module](https://elixir.bootlin.com/linux/latest/source/drivers/hid/usbhid/hid-pidff.c)
- [OpenFFBoard](https://github.com/Ultrawipf/OpenFFBoard).

## DISCLAIMER

> [!CAUTION]
> THE SOFTWARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
> WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO  EVENT SHALL THE AUTHORS
> OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
> OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
