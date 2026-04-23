# Arcade Freeplay Mods
Patches and documentation for arcade freeplay roms. These mods are intended for original hardware/games that did not originally have freeplay. In the modern day, many of these old arcade machines are in a home environment or in a freeplay location where coins are not required. Many people resort to drilling holes in the cabinet or modifying the cabinet. The goal of this repository is to provide software-based solutions so the physical cabinet does not have to be modified.

## Patch Statuses
Games can have one of four statuses:
- In Progress: mod is still being developed, it is expected to change.
- Not Working: mod is not working in one aspect. For example, it can be working in MAME but not work on real hardware for one reason or another.
- Working: mod is complete and is working in the appropriate platform.
- Untested: mod has not been tested on the appropriate platform, the mod is complete and tested is required.
  
|   **Game Name**  | **MAME Tested** | **Machine Tested** |
|:----------------:|:---------------:|:------------------:|
| Arm Wrestling    | Working         | Working            |
| Donkey Kong      | Working         | Working            |
| Donkey Kong Jr   | Working         | Working            |
| Donkey Kong 3    | Working         | Working            |
| Frogger          | Not Working     | Untested           |
| Head On N        | Working         | Working⁴           |
| Head On 2 (S.L.) | Working         | Working¹           |
| Heli Fire        | Working         | Working            |
| Mario Bros.      | Working         | Working            |
| Popeye           | Working         | Working²           |
| Pulsar           | Working         | Untested           |
| Radar Scope      | Working         | Working³           |
| Sky Skipper      | Working         | Working            |
| Space Demon      | Working         | Working            |
| Space Encounters | Working         | Working            |
| Zaxxon           | Working         | Working            |


1. Tested working on Nintendo Head On N hardware.
2. Popeye was tested on real hardware on a board that did not come with a populated security chip. Some boards have this chip and the mod will likely not work with this.
3. Radar Scope was tested working on real hardware with Revision D ROMs.
4. I wrote 3 patches for Head On N: Free Play, Upright, and Upright Freeplay. The upright mods have not been checked in yet because of how involved they were. *However, the cocktail freeplay ROM is tested working.*

## Known Bugs
### Popeye
**Febuary 1st 2026**: There is a graphics glitch that can happen on a real machine that does not show up in MAME. Sometimes after a gameover in 2p mode, text saying to start a game can appear after a game over. It is immediately cleared. It should not effect overall gameplay. The current theory is that the credit count isn't being cleared soon enough for that to not show up.

**Febuary 9th 2026**: Upon re-examining my code for auto-starting the game, I realize that it starts in an "uncontrolled way". It jumps into the middle of an instruction, the opcodes ends up being a jump to where it might need to go. It works but should probably be fixed.

### Frogger
**April 22nd 2026**: If you start a game during the demo, the death block location of the vehicles can be wrong.
