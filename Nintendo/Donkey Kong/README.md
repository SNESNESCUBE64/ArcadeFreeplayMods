# Donkey Kong Freeplay
This is a freeplay mod for several ROM sets for Donkey Kong. These patches are intended to be used with LunarIPS or similar patching utilities.

## Patch information
### Supported ROM Sets
| **ROM Set** | **MAME Working?** | **Machine Working?** |
|-------------|:-----------------:|:--------------------:|
| dkong       |        Yes        |          Yes         |
| dkonghrd    |        Yes        |       Untested       |
| dkongo      |        Yes        |       Untested       |
| dkongj      |        Yes        |       Untested       |
| dkongjo     |        Yes        |       Untested       |
| dkongjo1    |        Yes        |       Untested       |

### US Set 1 - dkong.zip
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location TKG4/TKG3** |
|----------------------|----------|---------------------|---------------------------|
| c_5at_g.bin          |    4k    |       92A564DA      |      5A/5K                |
| c_5et_g.bin          |    4k    |       EAC7A4E4      |      5E/5F                |

### US Set 1 (Hard) - dkonghrd.zip
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location TKG4/TKG3** |
|----------------------|----------|---------------------|---------------------------|
| dk5ahard.bin         |    4k    |       82354C81      |      5A/5K                |
| dk5ehard.bin         |    4k    |       F9F34E7A      |      5E/5F                |

### US Set 2 - dkongo.zip
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location TKG4/TKG3** |
|----------------------|----------|---------------------|---------------------------|
| tkg3c.5k             |    4k    |       7E9EB7A1      |      5A/5K                |
| c_5f_b.bin           |    4k    |       12F8377E      |      5E/5F                |

### Japan Set 1 - dkongj.zip
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location TKG4/TKG3** |
|----------------------|----------|---------------------|---------------------------|
| c_5k_b.bin           |    4k    |       12E85E1D      |      5A/5K                |
| c_5f_b.bin           |    4k    |       12F8377E      |      5E/5F                |

### Japan Set 2 - dkongjo.zip
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location TKG4/TKG3** |
|----------------------|----------|---------------------|---------------------------|
| c_5k_b.bin           |    4k    |       12E85E1D      |      5A/5K                |
| c_5f_b.bin           |    4k    |       12F8377E      |      5E/5F                |

### Japan Set 3 - dkongjo1.zip
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location TKG4/TKG3** |
|----------------------|----------|---------------------|---------------------------|
| 5k.bin               |    4k    |       52C46786      |      5A/5K                |
| c_5f_b.bin           |    4k    |       12F8377E      |      5E/5F                |

## Modification Documentation
### Noteworthy Places in Memory
- 6001: Credit Count
- 6003: Credit switch is held
- 6005: Game Mode
    - 0x00 = startup/not initialized
    - 0x01 = attract mode
    - 0x02 = credit screen, awaiting start
    - 0x03 = game mode
- 6007: Controls/Digital Sounds Enable
    - 0x01 = Disabled
    - 0x00 = Enabled
- 6080: Analog Sounds Queue
- 7D00: Controls
    - bit 7 = credit switch
    - bit 3 = 2P switch
    - bit 2 = 1P Start switch

### CPU ROM Addresses
| **Location** | **Start Address** | **Size** | **Chip Type** |
|:------------:|:-----------------:|:--------:|:-------------:|
| 5E/5F        | 0x0000            | 4k       | 2532          |
| 5C/5G        | 0x1000            | 4k       | 2532          |
| 5B/5H        | 0x2000            | 4k       | 2532          |
| 5A/5K        | 0x3000            | 4k       | 2532          |

### Added Routines
Many of these routines were added where the "Ikegami" text was located since that data is not referenced by anything. As nice as it would have been to keep this routine, it was a good place to add my routines.

Many of these routines were re-used from my Radar Scope free play ROM.

#### Credit/Freeplay Routine
```z80asm
0x3F40   ld hl, $6005    21 05 60  //Load the game mode to check if it in attract
0x3F43   ld a, (hl)      7E
0x3F44   and $02         E6 02     //See if we are in credit screen or game mode
0x3F46   ret nz          C0        //Return if we are not in attract mode
0x3F47   ld a, ($7D00)   3A 00 7D  //Read the controls
0x3F4A   and $0C         E6 0C     //See if 1P or 2P is pressed
0x3F4C   ret z           C8        //Return if neither have been pressed
0x3F4D   ld c, a         4F        //Copy the controls into b register for later use
0x3F4E   xor a           AF        //Clear A so we can clear other values
0x3F4F   inc (hl)        34        //Increment the game mode at $6005
0x3F50   inc hl          23        //Increment the address register to hl to $6007
0x3F51   inc hl          23
0x3F52   (hl), a         77        //Load game mode by clearing $6007
0x3F53   call $011C      CD 1C 01  //Clear the sound buffers
0x3F56   ld hl, $6001    21 01 60  //Load the credit count
0x3F59   inc (hl)        34        //Add the first credit
0x3F5A   ld a, c         79        //Load the previously read controls
0x3F5B   and $08         E6 08     //See if P2 game has been started
0x3F5D   jp z, $0906     CA 06 09  //If not P2 game, start P1 game
0x3F60   inc (hl)        34        //Increment second credit
0x3F61   jp $0919        C3 19 09  //Start a P2 game
```

#### Injected Routines
These were where all the lines of code that were changed inline for it to properly work.

- 0x017B  Ld a, $7D00  ->   Call $3F40
- 0x017E  bit 7,a      ->   and $00      //Never trigger the following code
- 0x0782  Values here were changed in order to always print "Push Players Buttons" on high score screen. There is a call immediately after to make it always print the 1 and 2 player button.

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

| **Hex** |         **String**        |
|:-------:|:-------------------------:|
|   0x00  |          [Blank?]         |
|   0x01  |          [Blank?]         |
|   0x02  |          [Blank?]         |
|   0x04  |     [Credit Pricing?]     |
|   0x05  |     [Player Coin Text]    |
|   0x0A  |   1 or 2 players button   |
|   0x0B  |      1 player button      |
|   0x0C  |            Push           |
|   0x14  |           Credit          |
|   0x15  |    [Top 2 High Scores]    |
|   0x16  |   [3rd Place High Score]  |
|   0x17  |   [4th Place High Score]  |
|   0x18  |   [5th Place High Score]  |
|   0x19  | [High Score Table Header] |
|   0x1B  |        Insert Coin        |
|   0x1C  |        Player Coin?       |
|   0x1E  |    [Nintendo Copyright]   |

Strings are stored in the ROM starting at 0x3000. Each string is terminated by the character 0x3F. So one way to have it print "Free Play" is to replace the credit text. What is nice is that the credit string has 4 blank characters at the end. They did this to clear the area on screen for the purpose of printing the credit count. As a result, it can be replaced with the Free Play text with no issues since the routine that prints the credit count has been removed.

```
Credit String: 0x36C1 - 13 22 15 14 19 24 10 10 10 10 3F
Replace with: 0x36C1 - 16 22 15 15 10 20 1C 11 29 10 3F
```

## Images
![Freeplay](Images/DKFreeplayScreenshot.png)