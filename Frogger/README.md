# Frogger Freeplay
This is a mod to original Konami Sega Set 1, Sega Set 2, and Sega Moon Cresta Hardware Frogger ROM sets. 

## Patch information
Four sets are provided for the *frogger*, *froggers1*, *froggers2*, *froggermc* ROM sets as found in MAME. It has been tested for this ROM set only and may not work on other revisions of Frogger. The patches are designed to be used with LunarIPS. 

### Konami Frogger (frogger.zip)
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| frogger.26           |    4k    |       4782EBBB      |       IC5       |
| frsm3.7              |    4k    |       8372F356      |       IC7       |

### Sega Frogger Set 1 (froggers1.zip)
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| epr-26.ic5           |    4k    |       4782EBBB      |       IC5       |
| epr-34.ic7           |    4k    |       C256B21D      |       IC7       |

### Sega Frogger Set 2 (froggers2.zip)
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| epr-1012.ic5         |    4k    |       9C6B97A9      |       IC5       |
| epr-1013a.ic6        |    4k    |       F3AF8D30      |       IC6       |
| epr-1015.ic8         |    4k    |       D2A9D453      |       IC8       |

### Sega Frogger Moon Cresta Hardware (froggermc.zip)
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| epr-1031.15          |    4k    |       8B67FE37      |       IC15      |
| epr-1033.33          |    4k    |       BB134551      |       IC33      |


## Modification Documentation (frogger and froggers1)
Note, this section is out of date. Some of these routines have been rewritten
### Noteworthy Places in Memory
- 0x83E1: Credit Count
- 0x83E2: Credit Switch Held
- 0x83E5: Player 1 life count
- 0x83E6: Player 2 life count
- 0x83BA: Game Status
   - 0x00: Attract Mode
   - 0x01: Game Mode
- 0xE000: Coin switch inputs
   - 0x80: Coin Switch 1 Mask
   - 0x40: Coin Switch 2 Mask
   - 0x04: Service Switch 2 Mask
- 0xE002: Start switch inputs
   - 0x80: P1 Switch Mask
   - 0x40: P2 Switch Mask

### Added Routines
#### Credit/Freeplay Routine
```z80asm
0x2DC9   Ld a, ($83BA)     3A BA 83   //Load the game state
0x2DCC   and a             A7         //See if we are in attract
0x2DCD   ret nz            C0         //Continue on if attract
0x2DCE   ld a, ($E002)     3A 02 E0   //Read the start inputs
0x2DD1   cpl               2F         //take the complement
0x2DD2   cp C0             E6 C0      //Only proceed if we read the start buttons
0x2DD4   ret z             C8         //skip if we do not have anything
0x2DD5   ld hl, 83BA       21 BA 83   //Load the attract variable
0x2DD8   ld (hl), 1        36 01      //Set the attract variable
0x2DDA   ld hl, 83E1       21 E1 83   //Load the credit count
0x2DDD   ld (hl), 0        36 00      //Clear the credit count
0x2DDF   rlca              07         //See if it is player 1
0x2DE0   jr c, $2DE3       38 01      //If player 1 only insert one credit
0x2DE2   inc (hl)          34         //Add player 2 credit
0x2DE3   inc (hl)          34         //Add player 1 credit
0x2DE4   ret               C9         //Go back to normal operation
```

#### Clear On-Screen Sprite Queue
```z80asm
0x2DE5   ld hl, 8000       21 00 80   //load sprite ram source, we need to clear it
0x2DE8   xor a             AF         //clear a so we can erase
0x2DE9   ld b, FF          06 FF      //It is 8000 - 80FF it seems
0x2DEB   ld (hl), a        77         //Clear the value
0x2DEC   inc hl            23         //next address
0x2DED   dec b             05         
0x2DEE   jr nz -04         20 FB      //Loop until we find the
0x2DF0   ld a, ($83E1)     3A E1 83   //Load the value we injected this code at 
0x2DF3   ret               C9
```

#### Write the "LAY" part of "FREE PLAY" where "CREDIT 00" was
```z80asm
//hl already has the proper address loaded
0x2DF4   ld (hl), 1C     36 1C      //Write 'L'
0x2DF6   ld l, 9F        2E 9F      //Load next address
0x2DF8   ld (hl), 11     36 11      //Write 'A'
0x2DFA   ld l, 7F        2E 7F      //Load next address
0x2DFC   ld (hl), 29     36 29      //Write 'Y'
0x2DFE   ret             C9
```

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


## Images
![Frogger FP1](Images/FroggerFP1.png)
![Frogger FP2](Images/FroggerFP2.png)
