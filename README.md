# ArcadeFreeplayMods
Patches and documentation for arcade freeplay roms

## Patch Statuses
|   **Game Name**  | **MAME Tested** | **Machine Tested** |
|:----------------:|:---------------:|:------------------:|
| Donkey Kong      | Working         | Working            |
| Donkey Kong Jr   | Working         | Working            |
| Head On N        | Working³        | Working⁴           |
| Head On 2 (S.L.) | Working         | Working¹           |
| Heli Fire        | Working         | Working            |
| Popeye           | Working         | Working²           |
| Pulsar           | Working         | Untested           |
| Radar Scope      | Working         | Working³           |
| Sky Skipper      | Working         | Untested           |
| Space Demon      | Working         | Working            |
| Space Encounters | Working         | Working            |


1. Tested working on Nintendo Head On N hardware.
2. Popeye was tested on real hardware on a board that did not come with a populated security chip. Some boards have this chip and the mod will likely not work with this.
3. Radar Scope was tested working on real hardware with Revision D ROMs.
4. I wrote 3 patches for Head On N: Free Play, Upright, and Upright Freeplay. The upright mods have not been checked in yet because of how involved they were. *However, the cocktail freeplay ROM is tested working.*

## Known Bugs
### Popeye
**Febuary 1st 2026**: There is a graphics glitch that can happen on a real machine that does not show up in MAME. Sometimes after a gameover in 2p mode, text saying to start a game can appear after a game over. It is immediately cleared. It should not effect overall gameplay. The current theory is that the credit count isn't being cleared soon enough for that to not show up.

**Febuary 9th 2026**: Upon re-examining my code for auto-starting the game, I realize that it starts in an "uncontrolled way". It jumps into the middle of an instruction, the opcodes ends up being a jump to where it might need to go. It works but should probably be fixed.