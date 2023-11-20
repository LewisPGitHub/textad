#text adventure

#checks and inventory
checks = {
'bed_check':0,
'door_check':0

}

inventory = {
    'key':0,
    'lockpick':0

}

options = ''

#first room puzzle
while checks.get('bed_check') == 0:
    options = input("what will you do ")
    
    if options == "menu":
            print('look, move, use, pickup')    
    if options == "look":
            print("you are on a bed arms shakeled in the corner of your eye you see a lock pick")
    elif options == "move":
            print("you attempt to move but your arms are shakeled ")
    elif options == "pickup":
        if inventory['lockpick'] == 0:
            print("you pick up the lockpick")
            inventory['lockpick'] = 1
        else:
            print("you have the lockpick")
    elif options == "yell":
        print('''you scream for help, for hours until your voice becomes horse, weakened from exhaustion you faint, 
          "you awaken on a bed arms and feet shakled, you attempt to wiggle free and you notice the left arm shackel was free and
           "as you look around you see a half empty glass of water and beside that writing on the walls be quite''')
    elif options == "use":
        if inventory['lockpick'] == 1:
            print("you unlock the shackles and you escape the bed")
            checks['bed_check'] = 1
        else:
            print("you do not have anymeans to unlock the shackles")


    
#open final door check
while checks.get('door_check') == 0:
    options = input("what will you do")
    if options == "key" and inventory.get('key') == 1:
        print("you open the door")
        checks["door_check"] = 1
    else:
        print("you do not open the door")
    