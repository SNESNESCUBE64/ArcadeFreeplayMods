# Stratovox Free Play
This is a mod to original Taito Licensed Stratovox ROMs that adds free play to the game. 

## Patch information
### Supported ROM Sets
| **ROM Set** | **MAME Working?** | **Machine Working?** |
|-------------|:-----------------:|:--------------------:|
| stratvox    |        Yes        |          Yes         |
| stratvoxa   |        Yes        |       Untested       |
| stratvoxb   |        Yes        |       Untested       |

### stratvox
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| ls01.bin             |    2k    |       13457EB8      |       4/5J      |
| ls06.bin             |    2k    |       BAC01655      |       11J       |

### stratvoxa
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| sv-1                 |    2k    |       13457EB8      |       4/5J      |
| sv-6                 |    2k    |       BAC01655      |       11J       |

### stratvoxb
| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| j0-1                 |    2k    |       3FCFA4E2      |       4/5J      |
| j0-6                 |    2k    |       C4789E0E      |       11J       |

## Modification Documentation
### Noteworthy Places in Memory
- 0x400E: Added for game mode
- 0x400F: Credit count
- 0x2F75: Constant 0x02, used in freeplay for print 2 in credit screen
- 0x5800: Start switch inputs
   - 0x80: P1 Switch Mask
   - 0x40: P2 Switch Mask

### Added Routines
#### Free Play Routine
```z80asm
Address  Instruction       Opcodes    Description
---------------------------------------------------------------------------
0x2F60   ld hl, $400E      21 0E 40   //Load the game state
0x2F63   ld a, (hl)        7E
0x2F64   and a             A7         //See if we are in a game
0x2F65   ret nz            C0         //Return if we are in a game
0x2F66   ld a, ($5800)     3A 00 58   //Load the start buttons
0x2F69   and $C0           E6 C0      //See if P1 or P2 was pressed
0x2F6B   ret z             C8         //Return if neither button is pressed
0x2F6C   inc (hl)          34         //Set the game mode
0x2F6D   inc hl            23         //Load the credit count
0x2F6E   inc (hl)          34         //Add the P1 coin
0x2F6F   rlca              07         //Check to see if P1 was pressed
0x2F70   jr c, $2F73       38 01      //If P1 is selected, skip P2 Credit
0x2F72   inc (hl)          34         //Add the P2 coin
0x2F73   xor a             AF         //Clear A for the return
0x2F74   ret               C9         //Return back to gameplay
```

#### Clear Game Status
```z80asm
Address  Instruction       Opcodes    Description
---------------------------------------------------------------------------
0x2F80   ld b, a           47         //Store a because it is needed later
0x2F81   xor a             AF         //Clear a to clear the game mode
0x2F82   ld ($400E), a     32 0E 40   //Clear the game mode
0x2F85   ld a, b           78         //Restore a back to what it was
0x2F86   call $061B        CD 1B 06   //From injected routine
0x2F89   ret               C9         
```

### Modified Routines
#### Autostart
```z80asm
Address  Instruction       Opcodes    Description
---------------------------------------------------------------------------
0x018F   nop               00         //Removed 'call $2124'
0x0190   nop               00
0x0191   nop               00
0x0192   ld hl, $400F      21 0F 40   //Read credit count instead of coin switch
0x0198   bit 0,b           CB 40      //Read bit 0 instead of bit 7
0x01A3   bit 1,b           CB 48      //Read bit 1 instead of bit 6
```

#### Single Instruction Modifications
```z80asm
0x040D   call 061B    -> call $2F80   //Call game mode clear routine
0x04D3   ld a, 5000   -> call $2F60   //Call FP routine instead read credit SW
0x07F9   ld hl, $400F -> ld hl, $2F75 //Refer to constant 02 instead of credit count
```

## Images
![Stratovox Free Play](Images/StratovoxFP.png)
