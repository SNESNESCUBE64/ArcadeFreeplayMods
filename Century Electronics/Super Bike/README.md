# Super Bike Freeplay
This is a freeplay with attract mod for Super Bike, a conversion kit for DK PCBs. These patches are meant to be used with LunarIPS or other similar patching utilities.

## Patch information
### Supported ROM Sets
| **ROM Set** | **MAME Working?** | **Machine Working?** |
|-------------|:-----------------:|:--------------------:|
| sbdk        |        Yes        |       Untested       |


### sbdk
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| sb-dk.ay             |    4k    |       965D4E59      |       5C        |
| sb-dk.ap             |    4k    |       EDA649EB      |       5E        |


## Modification Documentation
$1D9F - Credit Count

### Modifications
The methodology for the 2650 DK Kit Mods is very straight forward:
- Instead of printing credit count, load 40 credits into the credit count variable
- Replace "Credit" text with "Free Play"

## Images
![Freeplay](Images/SBFP_1.png)
