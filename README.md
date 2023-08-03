# TMC-EvalSystem

Trinamic Evaluation System ([home page](https://www.trinamic.com/support/eval-kits/))

[AN038: Using TRINAMIC’s IC Software API and Examples](https://www.trinamic.com/fileadmin/assets/Support/AppNotes/AN038_Using_TRINAMICs_IC_Software_API_and_Examples.pdf)

## Setup

To work on this repository use the following command in order to clone submodules recursively:
`git clone --recurse-submodules git@github.com:trinamic/TMC-EvalSystem.git`

## Cross Compile on Windows

### Requirements

* Make (There are a lot of ways to install Make on Windows, check out this blog post to see a few options you have: [https://www.technewstoday.com/install-and-use-make-in-windows/](https://www.technewstoday.com/install-and-use-make-in-windows/). Note that we are not responsible for the content on this website!)
* GNU Arm Embedded Toolchain: [https://developer.arm.com/downloads/-/gnu-rm](https://developer.arm.com/downloads/-/gnu-rm).

Make also sure the path to make and the toolchain's bin directory is also listed in your PATH environment variable.

### Build

Open the a Command Prompt, change the directory to the TMC-EvalSystem project and execute one of commands below.

If you want to use the pre-flashed bootloader on the Landungsbruecke and the TMCL-IDE to upload a new firmware (recommended) use:

* For the regular Landgsbruecke: `make all DEVICE=Landungsbruecke LINK=BL`
* For the LandgsbrueckeSmall: `make all DEVICE=LandungsbrueckeSmall LINK=BL`

When the build went through a hex-file should be available in the build directory (_build_Landungsbruecke or _build_LandungsbrueckeSmall) which can be uploaded to the Landungsbruecke using the TMCL-IDE

If you prefer to erase the pre-flashed bootloader and upload the firmware with a SWD programmer use:

* For the regular Landgsbruecke: `make all DEVICE=Landungsbruecke LINK=NOBL`
* For the LandgsbrueckeSmall: `make all DEVICE=LandungsbrueckeSmall LINK=NOBL`



## Changelog

For detailed changelog, see commit history.

### Version 3.08: (Released)
 * Added TMC2210, TMC2226, TMC2240, TMC2300, TMC6100-BOB, TMC6140, TMC6300 and TMC7300
 * Added support for Landungsbruecke Small (same PCB, different µC with less memory)
 * Added RAMDebug for TMC4671 to support automatic PI tuning
 * Removed TMC5161, TMC8690, TMCC160
 * Updated board detection mechanism
 * Various bugfixes & cleanups

### Version 3.07: (Released)
 * Added TMC2225 and TMC6100
 * Changed license from GPL to MIT
 * Improved API structure for UART-based boards
 * Various bugfixes & cleanups

### Version 3.06: (Released)
* Full TMC2160 support
* Landungsbruecke HW v2.0 support with internal HWID detection for future revisions
* Internal/external step/dir generator handling in FW and IDE
* Various bugfixes
* Internal optimizations

### Version 3.05: (Released)
* TMC5072-EVAL Critical bugfix at register access
* TMC2160-EVAL Corrected pin layout

### Version 3.02: (Released)
* Reworked chip register configuration mechanisms (generic reset/restore procedures implemented in API)
* Changed register accesses to use a unified Mask/Shift macro approach
* Various bugfixes
