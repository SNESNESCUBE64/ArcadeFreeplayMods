# Resolved Bugs
This section is a log for fixed bugs with patches. It is intended to act as archival from the main read me.

## Popeye
**Febuary 9th 2026**: Upon re-examining my code for auto-starting the game, I realize that it starts in an "uncontrolled way". It jumps into the middle of an instruction, the opcodes ends up being a jump to where it might need to go. It works but should probably be fixed.
- Issue was at 0x1F6F. There was a jump that jumped to 0x1F68 instead of 0x1F86. 0x1F68 is in the middle of an instruction which made it act in an unintended way. What was interesting is that it worked regardless of this. Patch has been updated to resolve this issue on 02 June 2026.

## Frogger
**April 22nd 2026**: If you start a game during the demo, the death block location of the vehicles can be wrong.
- Resolved by ensuring the correct spots in memory were cleared. When starting from demo mode, the game does not automatically clear the game RAM when starting the way I did, so extra code had to be added to clear out the correct spaces in memory. Patches have been updated to resolve this issue on 25 April 2026.