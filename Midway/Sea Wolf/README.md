# Sea Wolf Freeplay
This is a mod to original Sea Wolf ROMs that adds free play to the game. 

## Patch information
### Supported ROM Sets
| **ROM Set** | **MAME Working?** | **Machine Working?** |
|-------------|:-----------------:|:--------------------:|
| seawolf     |        Yes        |       Untested       |
| seawolfo    |        Yes        |       Untested       |
| seawolfa    |        Yes        |       Working        |

### Sea Wolf Set 1 - seawolf
|   **Patched ROM Name**   | **Size** | **CRC-32 Checksum** | **IC Location** |
|--------------------------|----------|---------------------|-----------------|
| sw0043.f                 |    1k    |       0CDA9835      |        F1       |
| sw0044.e                 |    1k    |       45086136      |        E1       |

### Sea Wolf Set 2 - seawolfo
|   **Patched ROM Name**   | **Size** | **CRC-32 Checksum** | **IC Location** |
|--------------------------|----------|---------------------|-----------------|
| 5.d1                     |   512    |       B0E54DBD      |        D1       |
| 6.c1                     |   512    |       71F33A72      |        C1       |
| 8.a1                     |   512    |       5C3CC32A      |        A1       |

### Sea Wolf Set 3 - seawolfa
|   **Patched ROM Name**   | **Size** | **CRC-32 Checksum** | **IC Location** |
|--------------------------|----------|---------------------|-----------------|
| 9316b-2801_9316b-g-sw.g1 |    2k    |       60982168      |        G1       |

## Modification Documentation
The modification is actually really simple. Sea Wolf attract mode will continue if there is a coin in. So the game just always needs to think that there is a coin. 

More documentation to do.

## Images
![Freeplay](Images/SWFP.png)