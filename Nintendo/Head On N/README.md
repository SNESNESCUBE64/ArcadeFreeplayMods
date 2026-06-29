# Head On N Free Play and Upright Mods
These are several mods for the original Head On N ROM Set. These are used for adding free play or turning the ROMs into an upright version of the game. Head On N only ever really existed as a cocktail table, so I wanted to make an upright version of the ROM set.

## Patch Information
These are designed for use with the *headonn* ROM set as found in MAME. It is not garunteed to work on anything else.

### Cocktail (Stock) Free Play Patch
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| rom.l4               |    1k    |       4E6299C2      |        L4       |

### Upright Patch

### Upright Free Play Patch

## Modification Documentation
### Noteworthy Places in Memory

### CPU ROM Addresses
| **Location** | **Start Address** | **Size** | **Chip Type** |
|:------------:|:-----------------:|:--------:|:-------------:|
| E4           | 0x0000            | 1k       | 2708          |
| F4           | 0x0400            | 1k       | 2708          |
| G4           | 0x0800            | 1k       | 2708          |
| H4           | 0x0C00            | 1k       | 2708          |
| I4           | 0x1000            | 1k       | 2708          |
| J4           | 0x1400            | 1k       | 2708          |
| K4           | 0x1800            | 1k       | 2708          |
| L4           | 0x1C00            | 1k       | 2708          |

### Added Routines
#### Credit/Free Play Routine
```Z80asm
0x1DD7   in a, ($02)     DB 02     //Read 1P Start register
0x1DD9   and $10         E6 10     //Check to see if it was pressed
0x1DDB   jp z, $5DE6     CA E6 5D  //Jump to 1p credit start routine
0x1DDE   in a, ($03)     DB 03     //Read 2P Start register
0x1DE0   and $20         E6 20     //Check to see if it was pressed
0x1DE2   jp z, $5DED     CA ED 5D  //Jump to 2P credit start routine
0x1DE5   ret             C9
0x1DE6   ld hl, $E4D8    21 D8 E4  //Load the Credit Count
0x1DE9   inc (hl)        34        //increment credit count
0x1DEA   jp $40D8        C3 D8 40  //Jump to the 1p game start routine
0x1DED   ld hl, $E4D8    21 D8 E4  //Load the Credit Count
0x1DF0   inc (hl)        34        //Increment Credit Count twice
0x1DF1   inc (hl)        34        
0x1DF2   jp $40A5        C3 A5 40  //Jump to the 2p game start routine
```

#### Injected Code
```Z80asm
0x1DB7   ld hl, $3230    21 30 32  
0x1DBA   Call $5DD7      CD D7 5D  //Call Free Play Routine
0x1DBD   nop             00
```

## Images
### Cocktail Table Free Play
![Freeplay](Images/HONFreeplayScreenshotCocktail.png)