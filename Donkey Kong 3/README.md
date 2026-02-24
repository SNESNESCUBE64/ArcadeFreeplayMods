# Donkey Kong 3 Free Play
This is a mod to original Donkey Kong 3 ROMs that moves the option of free play to the dip switches. It uses the unused dip switch setting 'L'. This is so that the game can boot to free play mode, eliminating the need to go into settings to enable free play.

*Note: The "Free Play" setting in the service menu will no longer work when the free play dip switch is set. It overrides the free play setting in memory*

## Patch information
Three patches are provided for the *dkong3* ROM set as found in MAME. It has been tested for this ROM set only and may not work on other revisions of Donkey Kong 3. The patches are designed to be used with LunarIPS. 


| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| dk3c.7b              |    8k    |       949E2D41      |        7B       |

## DIP Switch Setting
This is found on DPSW 2 on the game PCB. It uses switch L.

| **Coin/Credit** | **L** |
|----------------:|:-----:|
|       Free Play |   On  |


## Modification Documentation
Most of the work is done by the game already. There is already a very good free play mode. So it is just making it so that it is a DIP switch option.

### Memory Values of Interest
- 0x6BF0: Free Play Setting
    - 0x01: Free Play Enabled
    - 0x00: Coin Operation
- 0x7D00: DIP Switch Settings
    - 0x08: DIP Switch L

### Changed Source Code
This was really simple, it reads the free play setting at $129D normally, but I replace it with a routine to read the dip switches and write to $6BF0 (0x00 for coin play, 0x01 for Free Play). I replace some text that is not used or displayed in the game with the routine in question.

```z80asm
Addr     Instruction     Opcode
----------------------------------
0x0040   ld a, ($7D00)   3A 00 7D     //Read dip switch 2
0x0043   and $08         E6 08        //Compare only switch L       
0x0045   jr nz, $5FDA    20 04        //If it isn't the override setting, use what is in memory
0x0047   ld a, ($6BF0)   3A F0 6B     //Load the current free play setting
0x004A   ret             c9
0x004B   ld a, $01       3E 01        //Load the write value
0x004D   ld ($6BF0), a   32 F0 6B     //Write the free play status
0x0050   ret                          //Returns with FP status in register a

0x129D   Call $0040      CD 40 00     //Check to see if the free play dip switches are enabled
```

## Images
![Freeplay](Images/DK3FP.png)