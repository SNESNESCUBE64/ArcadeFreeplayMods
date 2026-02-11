# ArcadeFreeplayMods
Patches and documentation for arcade freeplay roms

## Patch Statuses
|   **Game Name**  | **MAME Tested** | **Machine Tested** |
|:----------------:|:---------------:|:------------------:|
| Donkey Kong      | Working         | Working            |
| Donkey Kong Jr   | Working         | Working            |
| Head On N        | N/A             | N/A                |
| Heli Fire        | Working         | Working            |
| Popeye           | Working         | Working¹           |
| Radar Scope      | Working         | Working²           |
| Space Demon      | Working         | Working            |
| Space Encounters | Working         | Working            |


1. Popeye was tested on real hardware on a board that did not come with a populated security chip. Some boards have this chip and the mod will likely not work with this.
2. Radar Scope was tested working on real hardware with Revision D ROMs.

## Known Bugs
### Popeye
**Febuary 1st 2026**: There is a graphics glitch that can happen on a real machine that does not show up in MAME. Sometimes after a gameover in 2p mode, text saying to start a game can appear after a game over. It is immediately cleared. It should not effect overall gameplay. The current theory is that the credit count isn't being cleared soon enough for that to not show up.

**Febuary 9th 2026**: Upon re-examining my code for auto-starting the game, I realize that it starts in an "uncontrolled way". It jumps into the middle of an instruction, the opcodes ends up being a jump to where it might need to go. It works but should probably be fixed.