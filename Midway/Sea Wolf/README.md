# Sea Wolf Freeplay
This is a mod to original Sea Wolf ROMs that adds free play to the game. 

*Note, these mods are still in progress. I am looking to see if there is a more efficient way of doing this.*

## Patch information
### Supported ROM Sets
| **ROM Set** | **MAME Working?** | **Machine Working?** |
|-------------|:-----------------:|:--------------------:|
| seawolf     |        Yes*       |       Untested       |
| seawolfo    |        No         |       Untested       |
| seawolfa    |        No         |       Untested       |

*Improvements are being investigated, too many ROMs need modification.

### seawolf
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| sw0042.g             |    1k    |       78B13F6A      |        G        |
| sw0043.f             |    1k    |       9FD646DE      |        F        |
| sw0044.e             |    1k    |       3C2F2733      |        E        |

## Modification Documentation
The modification is actually really simple. Sea Wolf attract mode will continue if there is a coin in. So the game just always needs to think that there is a coin. 

More documentation to do.

## Images
![Freeplay](Images/SWFP.png)