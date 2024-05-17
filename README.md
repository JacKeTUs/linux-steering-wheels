# Linux steering wheels FFB support

## Ranks

Ranks are totally subjective.

### Platinum

Works fully with the recommended driver with extensive testing. Most common FFB effects implemented.

### Gold

Works fully but it's less tested and there might be some minor issues. Most common FFB effects implemented.

### Silver

Works almost fully. Some FFB effects might be missing or some other significant issues which might be important in some cases. Workarounds could be available.

### Bronze

Major bugs or missing FFB effects which limit its use. It might be enough in some cases but it's far from fully working.

### Broken

The device might be recognized as a gamepad/joystick but there's no FFB.

### Not tested

Device not tested at all. May be working, may be not. Contributions welcome!

## Table of compatibility

| Manufacturer | Device names         | VID  | PID  | Support  | Protocol        | Proton compatibility |
|--------------|----------------------|------|------|----------|-----------------|--------------|
| Asetek       | Invicta              | 2433 | f300 |Not tested| ? | |
| Asetek       | Forte                | 2433 | f301 |Not tested| ? | |
| Asetek       | La Prima             | 2433 | f303 |Not tested| ? | |
| Asetek       | Tony Kannan          | 2433 | f306 |Not tested| ? | |
| Cammus       | C5                   | 3416 | 0301 | Silver   | hid-pidff[^1] | Works [1](#duration-issue), [2](#joystick-detection) |
| Fanatec      | CSL Elite            | 0eb7 | 0e03 | Gold     | hid-fanatecff[^7] | |
| Fanatec      | CSL Elite (PS4)      | 0eb7 | 0005 | Gold     | hid-fanatecff[^7] | |
| Fanatec      | DD                   | 0eb7 | 0020 | Gold     | hid-fanatecff[^7] | |
| Fanatec      | DD Pro               | 0eb7 | 0020 | Gold     | hid-fanatecff[^7] | |
| Fanatec      | Clubsport DD         | 0eb7 | 0020 | Gold     | hid-fanatecff[^7] | |
| Fanatec      |ClubSport Wheel Base V2|0eb7 | 0001 | Silver   | hid-fanatecff[^7] | |
| Fanatec      |ClubSport Wheel Base V2.5|0eb7|0004 | Silver   | hid-fanatecff[^7] | |
| Fanatec      | Podium DD1           | 0eb7 | 0006 | Silver   | hid-fanatecff[^7] | |
| Fanatec      | Podium DD2           | 0eb7 | 0007 | Silver   | hid-fanatecff[^7] | |
| Fanatec      | CSR Elite            | 0eb7 | 0011 | Silver   | hid-fanatecff[^7] | |
| Logitech     | MOMO Wheel           | 046d | c295 | Platinum | hid-logitech[^2] | Works |
| Logitech     | DFP                  | 046d | c298 | Platinum | hid-logitech[^2] | Works |
| Logitech     | DFGT                 | 046d | c29a | Platinum | hid-logitech[^2] | Works |
| Logitech     | G25                  | 046d | c29b | Platinum | hid-logitech[^2] | Works |
| Logitech     | G27                  | 046d | c29b | Platinum | hid-logitech[^2] | Works |
| Logitech     | G29                  | 046d | c24f | Platinum | hid-logitech[^2] | Works |
| Logitech     | G920                 | 046d | c262 | Silver   | hid-logitech-hidpp[^8] | Works |
| Logitech     | G923 (Xbox edition)  | 046d | c26d | Silver   | hid-logitech-hidpp[^8] | Works |
| Logitech     | G923 (PS edition)    | 046d | c267 | Platinum | hid-logitech[^3] | Works |
| Logitech     | G Pro                | 046d | c272 | Bronze   | hid-logitech-hidpp[^4] | Works [2](#joystick-detection) |
| Moza         | R3                   | 346e | 0005 | Silver   | hid-pidff | Needs testing [1](#duration-issue) |
| Moza         | R5                   | 346e | 0004 | Silver   | hid-pidff | Needs testing [1](#duration-issue) |
| Moza         | R9                   | 346e | 0002 | Silver   | hid-pidff | Needs testing [1](#duration-issue) |
| Moza         | R9v2                 | 346e | 0002 | Silver   | hid-pidff | Needs testing [1](#duration-issue) |
| Moza         | R12                  | 346e | 0006 | Silver   | hid-pidff | Needs testing [1](#duration-issue) |
| Moza         | R16                  | 346e | 0000 | Silver   | hid-pidff | Needs testing [1](#duration-issue) |
| Moza         | R21                  | 346e | 0000 | Silver   | hid-pidff | Needs testing [1](#duration-issue) |
| OpenFFBoard  |                    | 1209 | ffb0 | Silver | hid-pidff | Needs testing [1](#duration-issue) |
| PXN          |                      |      |      |Not tested| ? | |
| Simagic      | M10                  | 0483 | 0522 | Silver   | hid-pidff[^1] | Works. [1](#duration-issue)  |
| Simagic      | Alpha Mini           | 0483 | 0522 | Silver | hid-pidff[^5][^6] | Works. [1](#duration-issue) |
| Simagic      | Alpha                | 0483 | 0522 | Silver | hid-pidff[^5][^6] | Works. [1](#duration-issue) |
| Simagic      | Alpha Ultimate       | 0483 | 0522 | Silver | hid-pidff[^5][^6] | Works. [1](#duration-issue) |
| Simucube     | Simucube 1           | 16d0 | 0d5a | Silver | hid-pidff | Works[^10]. [How to setup Simucube base](https://granitedevices.com/wiki/Using_Simucube_wheel_base_in_Linux) |
| Simucube     | Simucube 2 Sport     | 16d0 | 0d61 | Silver | hid-pidff | Works[^10]. [How to setup Simucube base](https://granitedevices.com/wiki/Using_Simucube_wheel_base_in_Linux) |
| Simucube     | Simucube 2 Pro       | 16d0 | 0d60 | Silver | hid-pidff | Works[^10]. [How to setup Simucube base](https://granitedevices.com/wiki/Using_Simucube_wheel_base_in_Linux) |
| Simucube     | Simucube 2 Ultimate  | 16d0 | 0d5f | Silver | hid-pidff | Works[^10]. [How to setup Simucube base](https://granitedevices.com/wiki/Using_Simucube_wheel_base_in_Linux) |
| SimXperience | AccuForce Pro        | 1fc9 | 804c | Silver | hid-pidff |  |
| Thrustmaster | T248                 | 044f | b696 | Gold     | hid-tmff2[^9] | |
| Thrustmaster | T300RS (PS3 mode)    | 044f | b66e | Gold     | hid-tmff2[^9] | |
| Thrustmaster |T300RS (PS3 advanced mode)|044f|b66f| Gold     | hid-tmff2[^9] | |
| Thrustmaster | T300RS (PS4 mode)    | 044f | b66d | Gold     | hid-tmff2[^9] | |
| Thrustmaster | TX                   | 044f | b669 | Gold     | hid-tmff2[^9] | |
| Thrustmaster | TS-XV                | 044f |      | Gold     | hid-tmff2[^9] | |
| Turtle Beach |                      |      |      |Not tested| ? | |
| VRS          | DirectForce Pro      | 0483 | a355 |Broken    | hid-pidff[^7] | ? | |

[^1]: HID PID without a7 descriptor. Use [patched driver](https://github.com/spikerguy/cammus-ff).
[^2]: Default driver lacks most effects. Use [patched driver](https://github.com/berarma/new-lg4ff).
[^3]: Not supported by default driver. Use [patched driver](https://github.com/berarma/new-lg4ff).
[^4]: Not supported by default driver. Use [patched driver](https://github.com/JacKeTUs/hid-logitech-hidpp).
[^5]: HID PID with caveats. Use [patched driver](https://github.com/JacKeTUs/simagic-ff).
[^6]: Only firmware versions up to v159.
[^7]: HID descriptor does not allow to initialize FFB. See [JacKeTUs#4](https://github.com/JacKeTUs/linux-steering-wheels/issues/4) for information.
[^8]: Full USB command queue errors. Using [ffbwrap]() can help in some situations.
[^9]: Custom module [hid-tmff2](https://github.com/Kimplul/hid-tmff2).
[^10]: https://community.granitedevices.com/t/simucube-2-discussion-thread/2664/1606

## PIDFF caveats

### Duration issue

Due to value of "infinite duration" not explicitly defined in PIDFF protocol, we have a bug in pidff driver. Many apps (including Wine) uses 0 as 'infinite duration' effect. [Link to mailing list](https://lkml.org/lkml/2022/10/2/99)

To mitigate that issue you could use [ffbwrap](https://github.com/berarma/ffbtools) tool. For example, launch games with command:
`ffbwrap --duration-fix /dev/input/by-id/usb-Your-Wheel-event-joystick %command%`

### `a7` descriptor issue

Descriptor `0xa7` (effect delay) is not required for Windows PIDFF implementation. Some manufacturers (including Simucube at first, later Simagic and Cammus) didn't implement that parameter in their firmware. But in Linux PIDFF implementation `0xa7` descriptor is mandatory, and device without it can't be initialized with PIDFF driver. Simucube [fixed it in latest firmware (1.0.49)](https://granitedevices.com/wiki/SimuCUBE_firmware_releases).

Small fix, which removes `0xa7` descriptor from pidff, enables FFB in some devices (like Simagic and Cammus).

## Wine/Proton caveats

### Joystick detection

Even if device rank is "Native", there may be some small issues regarding SDL wheel detection in Steam. Now there is no possible way to euristically detect a wheel, so [SDL have whitelist](https://github.com/libsdl-org/SDL/blob/main/src/joystick/SDL_joystick.c#L340) of VID/PIDs.

Also, for devices not present in list, Steam uses sandboxed SDL1.2 to detect devices. It has one small rule to detect all kinds of joystics, function [EV_IsJoystick()](https://github.com/libsdl-org/SDL-1.2/blob/main/src/joystick/linux/SDL_sysjoystick.c#L382-L398). And basically, for the device to be classed as a joystick, it must have either X and Y axes or a X and Y hat, and must have a trigger, A button, or 1 button. On some devices Y axis not exists (Logitech G Pro), and therefore, for SDL, that device is not a joystick and no need to forward it to the game. Native apps will work perfectly, Wine apps too, but not Steam+Proton games. We could fix it by changing descriptor axis, something like rename Rz to Y, and wheel will work in Proton now

[Link to the Proton issue](https://github.com/ValveSoftware/Proton/issues/5126)

Also, recent updates to SDL created SDL Hint variable to dynamically extend wheel devices list[^15]. You need to just export `SDL_JOYSTICK_WHEEL_DEVICES=0x<VID>/0x<PID>,0x<VID2>/0x<PID2>` before you launching something.

## Steam settings for ~all devices and ~all games

1. Turn Steam Input off in game settings
2. Use recent Proton version for non-native games. 7 version known for having issues with HID devices detection. 
3. If game does not detect your device, try [setting SDL Hint](https://github.com/libsdl-org/SDL/issues/8595)environment variable in game launch command like so:
    ```
    SDL_JOYSTICK_WHEEL_DEVICES=0x<VID>/0x<PID> %command%
    ```
    This is only relevant for devices which are, for various reasons, not in a SDL whitelist[^14] (yet), or for older Steam runtime versions which does not have updated SDL library.

4. If none of that worked, create an issue, where members of the community will try to help you with your specific game

## Links

- [HID PID specification](https://www.usb.org/sites/default/files/documents/pid1_01.pdf).
- [Logitech FFb Protocol v1.6](https://opensource.logitech.com/wiki/force_feedback/Logitech_Force_Feedback_Protocol_V1.6.pdf).
- [hid-logitech-hidpp kernel module](https://elixir.bootlin.com/linux/latest/source/drivers/hid/hid-logitech-hidpp.c).
- [hid-pidff kernel module](https://elixir.bootlin.com/linux/latest/source/drivers/hid/usbhid/hid-pidff.c)
- [OpenFFBoard](https://github.com/Ultrawipf/OpenFFBoard).

## DISCLAIMER

THE SOFTWARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
