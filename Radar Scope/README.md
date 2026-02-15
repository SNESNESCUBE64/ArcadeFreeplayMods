# Radar Scope Freeplay
This is a mod to original C and D revisions of the TRS2 Radar Scope ROMs that adds free play to the game. 

## Patch information
Two patch files are provided for the *radarscpc* and *radarscp* ROM sets as found in MAME. It may not work on TRS1 board sets

### TRS2 Revision C - radarscpc
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| trs2c5fc             |    4k    |       0B4C782A      |        5F       |
| trs2c5hc             |    4k    |       5C4A71D5      |        5H       |

### TRS2 Revision D - radarscp
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| trs2c5fd             |    4k    |       CB632D94      |        5F       |
| trs2c5hd             |    4k    |       EE5F15D1      |        5H       |


## Modification Documentation
### Noteworthy Places in Memory
- 7D81: Grid Enable (write only)
    - 0xF0 to turn off the grid
- 7D00: Controls
    - bit 7 = credit switch
    - bit 3 = 2P switch
    - bit 2 = 1P Start switch
- 6001: Credit Count
- 6003: Credit switch is held
- 6005: Game Mode
    - 0x00 = startup/not initialized
    - 0x01 = attract mode
    - 0x02 = credit screen, awaiting start
    - 0x03 = game mode

### CPU ROM Addresses
| **Location** | **Start Address** | **Size** | **Chip Type** |
|:------------:|:-----------------:|:--------:|:-------------:|
| 5F           | 0x0000            | 4k       | 2532          |
| 5G           | 0x1000            | 4k       | 2532          |
| 5H           | 0x2000            | 4k       | 2532          |
| 5K           | 0x3000            | 4k       | 2532          |

### Added Routines
#### Credit/Freeplay Routine
```z80asm
0x2C00   ld a, ($6005)   3A 05 60  //Load the game mode to check if it in attract
0x2C03   and $02         E6 02     //See if we are in credit screen or game mode
0x2C05   ret nz          C0        //Return if we are not in attract mode
0x2C06   ld a, ($7D00)   3A 00 7D  //Read the controls
0x2C09   ld b, a         47        //Copy the controls into b register for later use
0x2C0A   and $0C         E6 0C     //See if player 1 or player 2 has been pressed
0x2C0C   ret z           C8        //If return if neither has been pressed
0x2C0D   ld hl, $7D81    21 81 7D  //Load the grid control address
0x2C10   (hl), $F0       36 F0     //Turn off the grid
0x2C12   ld hl, $6005    21 05 60  //Load the game mode
0x2C15   inc (hl)        34        //Set the game mode to credit screen mode
0x2C16   ld hl, $6001    21 01 65  //Load the credit count
0x2C19   inc (hl)        34        //Load one credit, needed for 1p start
0x2C1A   ld a, b         78        //Load the stored inputs
2x2C1B   and $08         E6 08     //See if player 2 was pressed
2x2C1D   jr z, $2C23     28 04     //Jump to player 1 start if player 2 wasn't pressed
2x2C1F   inc (hl)        34        //Add the second credit for 2P
2x2C20   jp $05EE        C3 EE 05  //Jump to player 2 start routine
2x2C23   jp $05DB        C3 DB 05  //Jump to player 1 start routine
```

#### Push to Start String interception functions
I didn't do the best job documenting this one. These two routines were used as part of intercepting the routines that write the coin text to the title screen and replacing it with the "push 1p or 2p start" text.
```z80asm
0x2C30   ld a, $1B       3E 1B     //Load the next string
0x2C32   cp e            BB
0x2C33   jr nz, $2C70    20 3B     //Jump to the exception
0x2C35   ld de, $060A    11 0A 06
0x2C38   call $1E00      CD 00 1E  //Call the string print routine
0x2C3B   inc e           1C

0x2C70   call $1E00      CD 00 1E  //Call the string print routine
0x2C73   ret             C9
```

#### Routine to print "Free Play" text
```z80asm
0x2C40   ld de, $2C60    11 60 2C  //Load the "Free Play" string start address
0x2C43   ld hl, $749F    21 9F 74  //Load the address for printing characters to screen
0x2C46   ld bc, $0020    01 20 00  //Load the offset
0x2C49   ld a, (de)      1A        //Load the character to be printed
0x2C4A   ld (hl), a      77        //Print the character to the screen
0x2C4B   inc de          13        //Increment the string address pointer
0x2C4C   add hl, bc      09        //Increment the screen address pointer
0x2C4D   ld a, (de)      1A        //Load the next character to be printed
0x2C4E   cp $FF          FE FF     //See if it is the end of the string (0xFF)
0x2C50   jp nz, $2C4A    C2 4A 2C  //If we still have characters to print, then loop
0x2C53   ret             C9
```

#### Injected Routines
These were where all the lines of code that were changed inline for it to properly work.

- 0x0471  Call $03AE   ->   Call $2C40
- 0x09A6  Call $1E00   ->   Call $2C30
- 0x22A1  Ld a, $7D00  ->   Call $2C00
- 0x22A4  bit 7,a      ->   and $00      //Never trigger the following code
- 0x232F  ld (hl), e   ->   nop
- 0x2332  ld (hl), d   ->   nop


### Character Table (Incomplete)
|  Hex | Character |
|:----:|:---------:|
| 0x10 |  [Space]  |
| 0x11 |     A     |
| 0x12 |     B     |
| 0x13 |     C     |
| 0x14 |     D     |
| 0x15 |     E     |
| 0x16 |     F     |
| 0x17 |     G     |
| 0x18 |     H     |
| 0x19 |     I     |
| 0x1A |     J     |
| 0x1B |     K     |
| 0x1C |     L     |
| 0x1D |     M     |
| 0x1E |     N     |
| 0x1F |     O     |
| 0x20 |     P     |
| 0x21 |     Q     |
| 0x22 |     R     |
| 0x23 |     S     |
| 0x24 |     T     |
| 0x25 |     U     |
| 0x26 |     V     |
| 0x27 |     W     |
| 0x28 |     X     |
| 0x29 |     Y     |
| 0x2A |     Z     |

Free Play = 16 22 15 15 10 20 1C 11 29

### String List (Likely Incomplete)
This was a list of strings of characters used by the game. It was used for printing text like "1 or 2 Players Button". I used this table to make sure that I was printing the "Push 1 or 2 players button" text to the screen at the appropriate time. It was better to re-use the logic that was already there. This list is  likely incomplete, but these were the ones I documented.

|  Hex |         String         |
|:----:|:----------------------:|
| 0x05 |         Credit         |
| 0x06 |    [Radar Section 1]   |
| 0x07 |    [Radar Section 2]   |
| 0x08 |    [Radar Section 3]   |
| 0x0A |  1 or 2 Players Button |
| 0x0B |     1 Player Button    |
| 0x0C |          Push          |
| 0x14 |        Credit 00       |
| 0x15 |   [Top 2 High Scores]  |
| 0x16 |    [3rd Place Score]   |
| 0x17 |    [4th Place Score]   |
| 0x18 |    [5th Place Score]   |
| 0x19 | Rank, Score, Name text |
| 0x1B |  [Coin Pricing Values] |
| 0x1C |       Insert Coin      |
| 0x1E |       © Nintendo       |
| 0x1F |          1980          |

- 2C60: Free Play String (backwards)
    - 29 11 1C 20 10 15 15 22 16

## Images
![Freeplay](Images/RSFreeplayScreenshot.png)