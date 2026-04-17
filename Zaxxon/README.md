# Space Encounters Freeplay
This is a mod to original Zaxxon Rev D ROMs that adds free play to the game. 

NOTE: This is still in progress. This patch is not finalized.

## Patch information
One patch are provided for the *zaxxon* ROM set as found in MAME. It has been tested for this ROM set only and may not work on other revisions of Zaxxon. The patches are designed to be used with LunarIPS. 


| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| zaxxon_rom3d.u27     |    8k    |       7534BE56      |        U27      |

## To do list
- replace "Credit 00" with "Free Play"
- replace "Insert Coin" phrase with "Push ..."
- rewrite coin routine to jump to game start if applicable.

## Modification Documentation
The freeplay mod was actually a weird one. The code has a suprising amount of similarities to Donkey Kong. For example, its game mode variable is exactly the same as DK. I want to investigate it a bit further.

### Noteworthy Places in Memory
- 6005: Game Mode
    - 0x00 = startup/not initialized
    - 0x01 = attract mode
    - 0x02 = credit screen, awaiting start
    - 0x03 = game mode

### Credit Routine
```z80asm
0x00A0   Ld a, ($6005)     3A 04 60   //Load the game state
0x00A3   cp 01             FE 01      //See if we are in attract
0x00A5   jr nz D8          20 31      //Continue on
0x00A7   ld a, ($C100)     3A 00 C1   //Read the start inputs
0x00AA   and 0c            E6 0C      //Only proceed if we read the start buttons
0x00AC   jr z D8           28 2A      //skip if we do not have anything
0x00AE   ld hl, 6012       21 12 60   //Load the credit count
0x00B1   ld (hl), 0        36 00      //Clear Credit Count
0x00B3   and 08            E6 08      //See if player 2 was held down
0x00B5   jr z 01           28 01      //1P game, so only load one credit
0x00B7   inc (hl)          34         //increment credit count
0x00B8   inc (hl)          34         //increment credit count
0x00B9   jr D8             18 1D      //Go back to normal operation
```

### Auto Start Routine
```z80asm
0x00BB   ld hl 6002        21 02 60   //Load our flag
0x00BE   ld a, hl          7E         //copy it to A
0x00BF   and a             A7         //If set
0x00C0   jr nz 02          20 02      //Jump to game start
0x00C2   inc (hl)          34         //Else set flag
0x00C3   ret               C9         //return back to start code, there is a weird glitch if it doesn't run at least once
0x00C4   ld (hl), 0        36 00      //clear the flag
0x00C6   ld a, 6012        3A 12 60   //load credit count
0x00C9   rla               17         //shift left twice to mimic controls
0x00CA   rla               17
0x00CB   ret               C9         //return back to start code
```

### Injected Routines
## Images
To do