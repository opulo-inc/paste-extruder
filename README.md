# LumenPnP Paste Extruder

This repository contains the source for a prototype paste extruder head for the LumenPnP.

![paste extrusion](./img/hero-paste.gif)

**This is a prototype design. It is still in development.**

This extruder head is designed for solder paste and ink dispensing applications. It quickly and easily replaces the left toolhead on any version LumenPnP. It has been used to apply conductive ink and Loctite GC-10 solder paste onto PCBs.

Controlling this toolhead is currently done using `leash`, a python libary for interfacing with the LumenPnP, which can be found [here](https://github.com/opulo-inc/leash). There's an example script in `./sw/extrude/extrude.py` that you can use as a starting point for your own application.

The CAD for the extruder is intended for a replacement left nozzle. However, the extruder requires a slightly different build of firmware that forces Z homing to occur at a different position, because otherwise the paste extruder will collide with `front-left-leg`. To prevent the extra step of flashing new firmware, the design is mirrored and intended mainly to be used as a replacement *left* nozzle. If exporting the 3D models yourself, be sure to mirror `extruder-base` and `cartridge-clamp` in your slicer before printing. All other models can be used normally.

## Parts

| Item | Quantity |
| ---- | -------- |
| [M3 Nut](https://www.mcmaster.com/90591A250/) | 1 |
| [M3 Threaded Rod](https://www.mcmaster.com/94595A215/) | 1 |
| [Nema 11 Stepper Motor (The higher current rating the better)](https://www.amazon.com/s?k=nema+11+stepper+motor) | 1 |
| [M2.5x5mm Socket Head Bolt](https://www.mcmaster.com/91290A100/) | 4 |
| [M3 Square Nut](https://www.mcmaster.com/97259A101/) | 1 |
| [M3x20mm Socket Head Bolt](https://www.mcmaster.com/91290A123/) | 1 |
| [3ml Luer Lock Syringe](https://www.mcmaster.com/7510A42/) | 1 |
| [Luer Lock Tip (size depends on application)](https://www.mcmaster.com/products/needles/fitting-connection~luer-lock/dispensing-tips-with-luer-lock-connection/tip-type~tapered/) | 1 |

## Install

Installation and setup instructions can be found in this video:

## Help

Feel free to hop in the [LumenPnP Discord Server](https://discordapp.com/invite/TCwy6De ) to help debug and troubleshoot using the extruder head. Also, please feel free to add Github Issues on this repository if you discover any problems.
