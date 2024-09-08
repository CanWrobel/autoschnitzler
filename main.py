import pyautogui
import time
import zustandWorldMap
import zustandLootbildschirm
import zustandInFight
import zustandLoserComp


while True:
    possiblyWorldmap = True
    possiblyAttackScreen = False
    possiblyLootScreen = False
    possiblyLoserComp = False
    while possiblyWorldmap:
        possiblyWorldmap = not zustandWorldMap.world_map()
        print(possiblyWorldmap)
        possiblyAttackScreen = not possiblyWorldmap
        possiblyLoserComp = False

    while possiblyAttackScreen:
        possiblyAttackScreen = not zustandInFight.in_fight()
        possiblyLootScreen = not possiblyAttackScreen

    while possiblyLootScreen:
        possiblyLootScreen = not zustandLootbildschirm.loot_bildschirm()
        possiblyWorldmap = not possiblyLootScreen
        possiblyLoserComp = True

    if possiblyLoserComp:
        possiblyLoserComp = not zustandLoserComp.loser_comp()

    
      

    


    print("Ausbruch aus Worldmap-Schleife")
        

