# Arcade Freeplay Mods
Patches and documentation for arcade freeplay roms. These mods are intended for original hardware/games that did not originally have freeplay. In the modern day, many of these old arcade machines are in a home environment or in a freeplay location where coins are not required. Many people resort to drilling holes in the cabinet or modifying the cabinet. The goal of this repository is to provide software-based solutions so the physical cabinet does not have to be modified.

## Patch Statuses
Games can have one of four statuses:
- In Progress: mod is still being developed, it is expected to change.
- Not Working: mod is not working in one aspect. For example, it can be working in MAME but not work on real hardware for one reason or another.
- Working: mod is complete and is working in the appropriate platform.
- Untested: mod has not been tested on the appropriate platform, the mod is complete and tested is required.

### Konami
|                              **Game Name**                           | **MAME Tested** | **Machine Tested** |
|:--------------------------------------------------------------------:|:---------------:|:------------------:|
| [Frogger](Konami/Frogger)                                            | Working         | Working            |

### Midway
|                              **Game Name**                           | **MAME Tested** | **Machine Tested** |
|:--------------------------------------------------------------------:|:---------------:|:------------------:|
| [Sea Wolf](Midway/Sea%20Wolf/)                                       | Working         | Untested           |
| [Space Encounters](Midway/Space%20Encounters/)                       | Working         | Working            |

### Namco
|                              **Game Name**                           | **MAME Tested** | **Machine Tested** |
|:--------------------------------------------------------------------:|:---------------:|:------------------:|
| [Bomb Bee](Namco/Bomb%20Bee/)                                        | Working         | Untested           |
| [Cutie Q](Namco/Cutie%20Q/)                                          | Working         | Untested           |
| [Pacman Plus](Namco/Pacman%20Plus/)                                  | Working         | Working⁴           |
| [Warp Warp](Namco/Warp%20Warp/)                                      | Working         | Untested           |

### Nintendo
|                              **Game Name**                           | **MAME Tested** | **Machine Tested** |
|:--------------------------------------------------------------------:|:---------------:|:------------------:|
| [Arm Wrestling](Nintendo/Arm%20Wrestling/)                           | Working         | Working            |
| [Donkey Kong](Nintendo/Donkey%20Kong/)                               | Working         | Working            |
| [Donkey Kong Jr](Nintendo/Donkey%20Kong%20Jr/)                       | Working         | Working            |
| [Donkey Kong 3](Nintendo/Donkey%20Kong%203/)                         | Working         | Working            |
| [Head On N](Nintendo/Head%20On%20N/)                                 | Working         | Working³           |
| [Heli Fire](Nintendo/Heli%20Fire/)                                   | Working         | Working            |
| [Mario Bros.](Nintendo/Mario%20Bros/)                                | Working         | Working            |
| [Popeye](Nintendo/Popeye/)                                           | Working         | Working²           |
| [Punch-Out!!](Nintendo/Punchout/)                                    | Working         | Working            |
| [Radar Scope](Nintendo/Radar%20Scope/)                               | Working         | Working            |
| [Sky Skipper](Nintendo/Sky%20Skipper/)                               | Working         | Working            |
| [Space Demon](Nintendo/Space%20Demon/)                               | Working         | Working            |
| [Space Fever](Nintendo/Space%20Fever/)                               | Working         | Untested           |
| [Space Fever HiSplitter](Nintendo/Space%20Fever%20HiSplitter/)       | Working         | Working            |
| [Space Firebird (Nintendo)](Nintendo/Space%20Firebird%20(Nintendo)/) | Working         | Working            |
| [Space Launcher](Nintendo/Space%20Launcher/)                         | Working         | Untested           |
| [Super Punch-Out!!](Nintendo/Super%20Punchout/)                      | Working         | Working            |

### Sega
|                              **Game Name**                           | **MAME Tested** | **Machine Tested** |
|:--------------------------------------------------------------------:|:---------------:|:------------------:|
| [Head On 2 (Sega Slimline)](Sega/Head%20On%202%20(Slimline)/)        | Working         | Working¹           |
| [Pulsar](Sega/Pulsar/)                                               | Working         | Untested           |
| [Turbo (Unencrypted ROMs)](Sega/Turbo/)                              | Working         | Untested           |
| [Zaxxon](Sega/Zaxxon/)                                               | Working         | Working            |

### Sun Electronics
|                              **Game Name**                           | **MAME Tested** | **Machine Tested** |
|:--------------------------------------------------------------------:|:---------------:|:------------------:|
| [Kangaroo](Sun%20Electronics/Kangaroo/)                              | Working         | Untested           |
| [Stratovox](Sun%20Electronics/Stratovox/)                            | Working         | Working            |



1. Tested working on Nintendo Head On N hardware.
2. Popeye was tested on real hardware on a board that did not come with a populated security chip. Some boards have this chip and the mod will likely not work with this.
3. I wrote 3 patches for Head On N: Free Play, Upright, and Upright Freeplay. The upright mods have not been checked in yet because of how involved they were. *However, the cocktail freeplay ROM is tested working.*
4. Tested working using encrypted version.

## Known Bugs
*None to currently report*
