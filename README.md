# Linux steering wheels FFB support


## Ranks
Ranks are totally subjective.

### Native
Device works perfectly out-of-the-box, no need to build/install any custom drivers.

Device gets 'Native' rank if device manufacturer uses known protocol (like PIDFF[^1]) or wrote driver for Linux (like hidpp[^10]).

### Platinum
FFB on a device works perfectly with custom driver, was tested by many users, every FFB effect implemented.

### Gold
Works with custom driver, without major bugs. May be not tested with many users/in all scenarios.

### Silver
Works with custom driver, may be not all FFB effects implemented. May be not tested with many users/in all scenarios. May be some caveats or bugs, refer to driver repo for information.

### Bronze
Basic FFB effects (like ConstantForce and Damper) works. Experimental support. Needs further testing. May be bugs, clipping, or memory leaks. Refer to driver repo for information.

### Broken
FFB doesn't work at all. Device uses proprietary protocol, not yet reverse-engineered

### Not tested
Device not tested at all. FFB protocol unknown. May be working, may be not. Contributions welcome!


## Table of compatibility
| Manufacturer | Device names         | VID  | PID  | Support  | Protocol        | Driver needed | Instructions (if needed)|
|--------------|----------------------|------|------|----------|-----------------|---------|--------------|
| Asetek       |                      |      |      |Not tested| ? | ? | |
| Cammus       | C5                   | 3416 | 0301 | Silver   | PIDFF[^1] without a7 descriptor | cammus-ff[^9] | |
| Fanatec      | CSL Elite            | 0eb7 | 0e03 | Gold     | Proprietary     | hid-fanatecff[^7] | |
| Fanatec      | CSL Elite (PS4)      | 0eb7 | 0005 | Gold     | Proprietary     | hid-fanatecff[^7] | |
| Fanatec      | DD                   | 0eb7 | 0020 | Gold     | Proprietary     | hid-fanatecff[^7] | |
| Fanatec      | DD Pro               | 0eb7 | 0020 | Gold     | Proprietary     | hid-fanatecff[^7] | |
| Fanatec      | Clubsport DD         | 0eb7 | 0020 | Gold     | Proprietary     | hid-fanatecff[^7] | |
| Fanatec      |ClubSport Wheel Base V2|0eb7 | 0001 | Silver   | Proprietary     | hid-fanatecff[^7] | |
| Fanatec      |ClubSport Wheel Base V2.5|0eb7|0004 | Silver   | Proprietary     | hid-fanatecff[^7] | |
| Fanatec      | Podium DD1           | 0eb7 | 0006 | Silver   | Proprietary     | hid-fanatecff[^7] | |
| Fanatec      | Podium DD2           | 0eb7 | 0007 | Silver   | Proprietary     | hid-fanatecff[^7] | |
| Fanatec      | CSR Elite            | 0eb7 | 0011 | Silver   | Proprietary     | hid-fanatecff[^7] | |
| Logitech     | MOMO Wheel           | 046d | c295 | Platinum | Logitech FF[^2] | hid-lg4ff (limited effects)<br>new-lg4ff[^3] | |
| Logitech     | DFP                  | 046d | c298 | Platinum | Logitech FF[^2] | hid-lg4ff (limited effects)<br>new-lg4ff[^3] | |
| Logitech     | DFGT                 | 046d | c29a | Platinum | Logitech FF[^2] | hid-lg4ff (limited effects)<br>new-lg4ff[^3] | |
| Logitech     | G25                  | 046d | c29b | Platinum | Logitech FF[^2] | hid-lg4ff (limited effects)<br>new-lg4ff[^3] | |
| Logitech     | G27                  | 046d | c29b | Platinum | Logitech FF[^2] | hid-lg4ff (limited effects)<br>new-lg4ff[^3] | |
| Logitech     | G29                  | 046d | c24f | Platinum | Logitech FF[^2] | hid-lg4ff (limited effects)<br>new-lg4ff[^3] | |
| Logitech     | G920                 | 046d | c262 | Native   | Logitech FF[^2] with HIDPP | hid-logitech-hidpp[^10] | |
| Logitech     | G923 (Xbox edition)  | 046d | c26d | Native   | Logitech FF[^2] with HIDPP | hid-logitech-hidpp[^10] | |
| Logitech     | G923 (PS edition)    | 046d | c267 | Platinum | Logitech FF[^2] | new-lg4ff | |
| Logitech     | G Pro                | 046d | c272 | Bronze   | Logitech FF[^2] with HIDPP | hid-logitech-hidpp with patches[^4] | |
| Moza         | R3                   | 346e | 0005 | Native   | PIDFF[^1] | pidff[^11] | |
| Moza         | R5                   | 346e | 0004 | Native   | PIDFF[^1] | pidff[^11] | |
| Moza         | R9                   | 346e | 0002 | Native   | PIDFF[^1] | pidff[^11] | |
| Moza         | R9v2                 | 346e | 0002 | Native   | PIDFF[^1] | pidff[^11] | |
| Moza         | R12                  | 346e | 0006 | Native   | PIDFF[^1] | pidff[^11] | |
| Moza         | R16                  | 346e | 0000 | Native   | PIDFF[^1] | pidff[^11] | |
| Moza         | R21                  | 346e | 0000 | Native   | PIDFF[^1] | pidff[^11] | |
| OpenFFBoard[^6]|                    | 1209 | ffb0 | Native   | PIDFF[^1] | pidff[^11] | |
| PXN          |                      |      |      |Not tested| ? | ? | |
| Simagic      | M10                  | 0483 | 0522 | Silver   | PIDFF[^1] without a7 descriptor  | simagic-ff[^5] | |
| Simagic      | Alpha Mini           | 0483 | 0522 | Silver (up to fw v159)<br>Broken | PID without a7 descriptor (up to fw v159)<br>Proprietary | simagic-ff[^5] | |
| Simagic      | Alpha                | 0483 | 0522 | Silver (up to fw v159)<br>Broken | PID without a7 descriptor (up to fw v159)<br>Proprietary | simagic-ff[^5] | |
| Simagic      | Alpha Ultimate       | 0483 | 0522 | Silver (up to fw v159)<br>Broken | PID without a7 descriptor (up to fw v159)<br>Proprietary | simagic-ff[^5] | |
| Simucube     | Simucube 1           | 16d0 | 0d5a | Native   | PIDFF[^1] | pidff[^11] | [How to setup Simucube base ](https://granitedevices.com/wiki/Using_Simucube_wheel_base_in_Linux) |
| Simucube     | Simucube 2 Sport     | 16d0 | 0d61 | Native   | PIDFF[^1] | pidff[^11] | [How to setup Simucube base ](https://granitedevices.com/wiki/Using_Simucube_wheel_base_in_Linux) |
| Simucube     | Simucube 2 Pro       | 16d0 | 0d60 | Native   | PIDFF[^1] | pidff[^11] | [How to setup Simucube base ](https://granitedevices.com/wiki/Using_Simucube_wheel_base_in_Linux) |
| Simucube     | Simucube 2 Ultimate  | 16d0 | 0d5f | Native   | PIDFF[^1] | pidff[^11] | [How to setup Simucube base ](https://granitedevices.com/wiki/Using_Simucube_wheel_base_in_Linux) |
| SimXperience | AccuForce Pro        | 1fc9 | 804c | Native   | PIDFF[^1]  | pidff[^11] |  |
| Thrustmaster | T248                 | 044f | b696 | Gold     | Proprietary| hid-tmff2[^8] | |
| Thrustmaster | T300RS (PS3 mode)    | 044f | b66e | Gold     | Proprietary| hid-tmff2[^8] | |
| Thrustmaster |T300RS (PS3 advanced mode)|044f|b66f| Gold     | Proprietary| hid-tmff2[^8] | |
| Thrustmaster | T300RS (PS4 mode)    | 044f | b66d | Gold     | Proprietary| hid-tmff2[^8] | |
| Thrustmaster | TX                   | 044f | b669 | Gold     | Proprietary| hid-tmff2[^8] | |
| Thrustmaster | TS-XV                | 044f |      | Gold     | Proprietary| hid-tmff2[^8] | |
| Turtle Beach |                      |      |      |Not tested| ? | ? | |
| VRS          | DirectForce Pro      |      |      |Not tested| ? | ? | |


[^1]: https://www.usb.org/sites/default/files/documents/pid1_01.pdf
[^2]: https://opensource.logitech.com/wiki/force_feedback/Logitech_Force_Feedback_Protocol_V1.6.pdf
[^3]: https://github.com/berarma/new-lg4ff
[^4]: https://github.com/JacKeTUs/hid-logitech-hidpp
[^5]: https://github.com/JacKeTUs/simagic-ff
[^6]: https://github.com/Ultrawipf/OpenFFBoard
[^7]: https://github.com/gotzl/hid-fanatecff
[^8]: https://github.com/Kimplul/hid-tmff2
[^9]: https://github.com/spikerguy/cammus-ff
[^10]: https://elixir.bootlin.com/linux/latest/source/drivers/hid/hid-logitech-hidpp.c
[^11]: https://elixir.bootlin.com/linux/latest/source/drivers/hid/usbhid/hid-pidff[^11].c



## PIDFF caveats
### Duration issue
Due to value of "infinite duration" not explicitly defined in PIDFF protocol, we have a bug in pidff driver. Many apps (including Wine) uses 0 as 'infinite duration' effect. [Link to mailing list](https://lkml.org/lkml/2022/10/2/99)

To mitigate that issue you could use ffbwrap[^12] tool. For example, launch games with command:
`ffbwrap --duration-fix /dev/input/by-id/usb-Your-Wheel-event-joystick %command%`

[^12]: https://github.com/berarma/ffbtools

### `a7` descriptor issue
Descriptor `0xa7` (effect delay) is not required for Windows PIDFF implementation. Some manufacturers (including Simucube at first, later Simagic and Cammus) didn't implement that parameter in their firmware. But in Linux PIDFF implementation `0xa7` descriptor is mandatory, and device without it can't be initialized with PIDFF driver. Simucube fixed it in latest firmware (1.0.49)[^13]

Small fix, which removes `0xa7` descriptor from pidff, enables FFB in some devices (like Simagic and Cammus).

[^13]: https://granitedevices.com/wiki/SimuCUBE_firmware_releases


## Wine/Proton caveats

### Joystick detection
Even if device rank is "Native", there may be some small issues regarding SDL wheel detection in Steam. Now there is no possible way to euristically detect a wheel, so SDL have whitelist[^14] of VID/PIDs.

[^14]: https://github.com/libsdl-org/SDL/blob/main/src/joystick/SDL_joystick.c#L340

Also, for devices not present in list, Steam uses sandboxed SDL1.2 to detect devices. It has one small rule to detect all kinds of joystics, function [EV_IsJoystick()](https://github.com/libsdl-org/SDL-1.2/blob/main/src/joystick/linux/SDL_sysjoystick.c#L382-L398). And basically, for the device to be classed as a joystick, it must have either X and Y axes or a X and Y hat, and must have a trigger, A button, or 1 button. On some devices Y axis not exists (Logitech G Pro), and therefore, for SDL, that device is not a joystick and no need to forward it to the game. Native apps will work perfectly, Wine apps too, but not Steam+Proton games. We could fix it by changing descriptor axis, something like rename Rz to Y, and wheel will work in Proton now

[Link to the Proton issue](https://github.com/ValveSoftware/Proton/issues/5126)



## DISCLAIMER

THE SOFTWARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.