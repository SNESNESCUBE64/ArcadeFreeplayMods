# Frogger Freeplay
This is a mod to original Konami, Sega Set 1, Sega Set 2, and Sega Moon Cresta Hardware Frogger ROM sets. 

## Patch information
### Supported ROM Sets
| **ROM Set** | **MAME Working?** | **Machine Working?** |
|-------------|:-----------------:|:--------------------:|
| frogger     |        Yes        |       Untested       |
| froggermc   |        Yes        |          Yes         |
| froggers1   |        Yes        |       Untested       |
| froggers2   |        Yes        |       Untested       |

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
| epr-1012.ic5         |    4k    |       9CF81379      |       IC5       |
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

## Modification Documentation (froggers2)

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
#### Credit/Freeplay Routine + Initialization
```z80asm
0x106B   Ld a, ($83BA)     3A BA 83   //Load the game state
0x106E   and a             A7         //See if we are in attract
0x106F   ret nz            C0         //Continue on if attract
0x1070   ld a, ($E002)     3A 02 E0   //Read the start inputs
0x1073   cpl               2F         //take the complement
0x1074   and $C0           E6 C0      //Only proceed if we read the start buttons
0x1076   ret z             C8         //skip if we do not have anything
0x1077   ld hl, $83E1      21 E1 83   //Load credit count
0x107A   ld (hl), $00      36 00      //Clear the credit count
0x107C   rlca              07         //See if it was 1P
0x107D   jr c, $1080       36 01      //It is player 1, only insert one coin
0x107F   inc (hl)          34         //Insert player 2 credit
0x1080   inc (hl)          34         //Insert player 1 credit

//Startup and Memory clearing
0x1081   ld hl, 8000       21 00 80   //load sprite ram source, we need to clear it
0x1084   xor a             AF         //clear a so we can erase
0x1085   ld c, $03         0E 03      //Clear $8000 - $819A
0x1087   ld b, $88         06 88
0x1089   ld (hl), a        77
0x108A   inc hl            23
0x108B   dec b             05
0x108C   jr nz, $1089      20 FB
0x108E   dec c             0D
0x108F   jr nz, $1087      20 F6
0x1091   ld (hl), a        77
0x1092   inc hl            23
0x1093   ld (hl), a        77
0x1094   inc hl            23
0x1095   ld hl, $825B      21 5B 82   //Clear $825B - $82A0
0x1098   ld b, $45         06 45
0x109A   ld (hl), a        77
0x109B   inc hl            23
0x109C   dec b             05
0x109D   jr nz, $109A      20 FB
0x109F   ld hl, $81A6      21 A6 81   //Clear $81A6 - $8254
0x10A2   ld b, $AE         06 AE
0x10A4   ld (hl), a        77
0x10A5   inc hl            23
0x10A6   dec b             05
0x10A7   jr nz, $10A4      20 FB

//Initialization
0x10A9   ld a, $05         3E 05
0x10AB   ld ($83D6), a     32 D6 83
0x10AE   xor a             AF
0x10AF   ld ($83D8), a     32 D8 83
0x10B2   ld hl, $83BA      21 BA 83
0x10B5   ld (hl), $01      36 01
0x10B7   ret               C9         //Go back to normal operation
```

#### Write the "LAY" part of "FREE PLAY" where "CREDIT 00" was
```z80asm
//hl already has the proper address loaded
0x1060   ld (hl), 1C     36 1C      //Write 'L'
0x1062   ld l, 9F        2E 9F      //Load next address
0x1064   ld (hl), 11     36 11      //Write 'A'
0x1066   ld l, 7F        2E 7F      //Load next address
0x1068   ld (hl), 29     36 29      //Write 'Y'
0x106A   ret             C9
```

### Injected Routines
#### Autostart Routine
```z80asm
0x0390   ld a, ($83E1)     3A E1 83   //Load the credit count
0x0393   rrca              0F         //See if P1
0x0394   jr c, $039D       38 07      //Jump to P1 routine
0x0396   rrca              0F         //See if P2
0x0397   jr nc, $0354      20 BB      //If it isn't P2 game, loop around
```

#### Print Freeplay
```z80asm
0x0BAF   ld hl, $A8BF      21 BF A8   
0x0BB2   Call $1060        CD 60 10   //print "LAY"
0x0BB5   ret               C9
```

#### Call Freeplay Routine
```z80asm
0x3E05   Call 106B         CD 6B 10   //Call Freeplay Routine
0x3E08   ret               C9
```

0xFF2 - 0x1004: Free play string updates


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
