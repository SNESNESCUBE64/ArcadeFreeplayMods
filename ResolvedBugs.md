# Resolved Bugs
This section is a log for fixed bugs with patches. It is intended to act as archival from the main read me.

## Popeye
**Febuary 1st 2026**: There is a graphics glitch that can happen on a real machine that does not show up in MAME. Sometimes after a gameover in 2p mode, text saying to start a game can appear after a game over. It is immediately cleared. It should not effect overall gameplay. The current theory is that the credit count isn't being cleared soon enough for that to not show up.
- Could not recreate issue after fixing the auto-start bug below. Perhaps the incorrect credit count was occasionally happening due to not properly auto-starting. Patch has been updated to resolve this issue on 02 June 2026.

**Febuary 9th 2026**: Upon re-examining my code for auto-starting the game, I realize that it starts in an "uncontrolled way". It jumps into the middle of an instruction, the opcodes ends up being a jump to where it might need to go. It works but should probably be fixed.
- Issue was at 0x1F6F. There was a jump that jumped to 0x1F68 instead of 0x1F86. 0x1F68 is in the middle of an instruction which made it act in an unintended way. What was interesting is that it worked regardless of this. Patch has been updated to resolve this issue on 02 June 2026.

## Frogger
**April 22nd 2026**: If you start a game during the demo, the death block location of the vehicles can be wrong.
- Resolved by ensuring the correct spots in memory were cleared. When starting from demo mode, the game does not automatically clear the game RAM when starting the way I did, so extra code had to be added to clear out the correct spaces in memory. Patches have been updated to resolve this issue on 25 April 2026.

**June 18th 2026**: 2P game does not work with froggers2 ROM set.
- at 0x397, a JR if carry was used instead of a JR if no carry. This seemed to be a miss from when the mod was ported from froggers1.
