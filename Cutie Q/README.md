# Cutie Q Freeplay
This is a mod to original Cutie Q ROMs that adds attract mode to the free play setting. It can be used with credits enabled as well as free play mode. These patches are meant to be used with LunarIPS or other similar patching utilities.

## Patch information
### Supported ROM Sets
| **ROM Set** | **MAME Working?** | **Machine Working?** |
|-------------|:-----------------:|:--------------------:|
| cutieq      |        Yes        |       Untested       |


| **Patched ROM Name** | **Size** | **CRC-32 Checksum** | **IC Location** |
|----------------------|----------|---------------------|-----------------|
| cutieq.1k            |    8k    |       64BE3A12      |        1k       |

## DIP Switch Setting
This is found on DPSW 1 on the game PCB. It uses switches 1 and 2.

| **Coin/Credit** | **1** | **2** |
|----------------:|:-----:|:-----:|
|             2/1 |   On  |  Off  |
|             1/1 | *Off* | *Off* |
|             1/2 |  Off  |   On  |
|       Free Play |   On  |   On  |


## Modification Documentation
To Do


## Images
![Freeplay](Images/CQFP.png)
