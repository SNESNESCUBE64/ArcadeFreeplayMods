# Hunchback Freeplay
This is a freeplay with attract mod for Hunchback, a conversion kit for DK PCBs. These patches are meant to be used with LunarIPS or other similar patching utilities.

## Patch information
### Supported ROM Sets
| **ROM Set** | **MAME Working?** | **Machine Working?** |
|-------------|:-----------------:|:--------------------:|
| hunchbdk    |        Yes        |       Untested       |


### hunchbdk
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| hb.5a                |    4k    |       2E272C5F      |       5A        |
| hb.5b                |    4k    |       2C19F0AC      |       5B        |
| hb.5e                |    4k    |       F568427E      |       5E        |


## Modification Documentation
### Noteworthy Locations in Memory
$1D98 - Credit Count

### Modifications
The methodology for the 2650 DK Kit Mods is very straight forward:
- Return instead of printing the credit digits
- Replace any load of the credit count with an immediate load of $99
- Replace "Credit" text with "Free Play"

## Images
![Freeplay](Images/HBFP_1.png)
