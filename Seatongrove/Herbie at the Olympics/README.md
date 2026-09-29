# Herbie at the Olympics Freeplay
This is a freeplay with attract mod for Herbie at the Olympics aka Hunchback Olympics, a conversion kit for DK PCBs and CVS System. These patches are meant to be used with LunarIPS or other similar patching utilities.

## Patch information
### Supported ROM Sets
| **ROM Set** | **MAME Working?** | **Machine Working?** |
|-------------|:-----------------:|:--------------------:|
| herbiedk    |        Yes        |       Untested       |
| huncholy    |        Yes        |       Untested       |


### herbiedk - Donkey Kong Conversion Kit
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| 5g.cpu               |    4k    |       97DFB8E2      |      5G/5C      |

### huncholy - CVS System
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| ho-gp2.bin           |    2k    |       AB709E5E      |                 |
| ho-gp3.bin           |    2k    |       65FB7F39      |                 |


## Modification Documentation
### Noteworthy Locations in Memory
$1C55 - Coin Switch Mirror
$1E50 - Credit Count (DK Kit)
$1E6A - Credit Count (hunchback olympics)

### Modifications
The methodology for the 2650 DK Kit Mods is very straight forward:
- Instead of printing credit count, load 40 credits into the credit count variable
- Replace "Credit" text with "Free Play"

## Images
![Freeplay](Images/HFP_1.png)
![Freeplay](Images/HBO_FP.png)
