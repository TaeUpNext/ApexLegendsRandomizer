import random 

class PickLegend:
    global legends
    legends = ["Ash", "Bangalore", "Bloodhound", "Caustic", "Crypto", "Fuse", "Gibraltar", "Horizon", "Lifeline", "Loba", "Mad Maggie", "Mirage", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer","Valkyrie", "Wattson"]#list of all the current legends, may need to be updated in the future
    
    def shuffle():
        for i in range(len(legends)-1, 0, -1):
            #pick a random index from 0 to i 
            j = random.randint(0, i +1)
            #swap arr[i] with the element at random index 
            legends[i], legends[j] = legends[j], legends[i]
            
    def choose_legend():
        firstChoice = legends[0] #displays legend at index 0 in the legends list
        secondaryChoice = legends[1]#displays legend at index 1 in the legends list
        lastChoice = legends[2]#displays legend at index 2 in the legends list
        
        print(f"\n First Choice (MUST USE THIS IF AVAILABLE): {firstChoice} \n Second Choice (Only use if 1st option is not available): {secondaryChoice} \n Third Choice (ONLY USE IF first 2 choices ARE NOT AVAILABLE): {lastChoice}")
        

class PickLoadout:
    global loadout
    loadout = ["Havoc Rifle", "VK-47 Flatline", "Hemlok Burst AR", "R-301 Carbine", "Alternator SMG", "Prowler Burst PDW", "R-99", "Volt SMG", "C.A.R. SMG", "Devotion LMG", "L-Star EMG", "M600 Spitfire", "Rampage LMG", "G7 Scout", "Triple Take", "30-30 Repeater", "Bocek Compund Bow", "Charge Rifle", "Longbow DMR", "Kraber .50-Cal Sniper", "Sentinel","EVA-8 Auto", "Mastiff Shotgun", "Mozambique Shotgun", "Peacekeaper", "RE-45", "P2020", "Wingman"] # a list of all current guns in apex legends, may need to be updated in the future 

    def shuffle(): #Fisher-Yates shuffle method
        for i in range(len(loadout)-1, 0, -1):
            #pick a random index from 0 to i 
            j = random.randint(0, i +1)
            #swap arr[i] with the element at random index 
            loadout[i], loadout[j] = loadout[j], loadout[i]
            
    def choose_loadout():
        primaryGun = loadout[0] #displays gun at index 0 in the loadout list
        secondaryGun = loadout[1] #displays gun at index 1 in the loaoduts list
        backupGun = loadout[2] #displays gun at index 2 in the loadouts

        print(f"\n Primary Gun: {primaryGun} \n Secondary Gun: {secondaryGun}\n Backup Gun (Only if one of the first two are CP guns): {backupGun}")


#Determine what user wants to generate
randomChoice = int(input("\nWould you like to randomly generate a legend, a loadout or both? Enter 1 for a legend, 2 for a gun or 3 for both: ") )
rc = randomChoice #variable that replaces randomChoice with rc

if rc == 1: #choice to start picking the legend
    plg = PickLegend
    plg.shuffle() #shuffles the legends list 
    print("\n**********************************************************************************")
    plg.choose_legend()
    print("\n**********************************************************************************")
    stop = False
    while not stop:
        stopCheck = int(input("\nWould you like to pick a another legend or are you done? Enter 1 to pick another legend or 2 to stop: "))
        if stopCheck == 1: #user wants to pick a loadout now too so it picks one for them
            plg = PickLegend
            plg.shuffle() #shuffles the legends list 
            print("\n**********************************************************************************")
            plg.choose_legend() 
            print("\n**********************************************************************************")
        elif stopCheck ==2: #user does not want to pick a loadout and it ends the program
            stop = True
            print("\n Program finished good luck in the Outlands Legend")



elif rc == 2: #choice to start picking the loadout 
    pld = PickLoadout
    pld.shuffle() #shuffles the loadouts list 
    print("\n**********************************************************************************")
    pld.choose_loadout()
    print("\n**********************************************************************************")
    stop = False
    while not stop:
        stopCheck = int(input("\nWould you like to pick a another loadout or are you done? Enter 1 to pick another legend or 2 to stop: "))
        if stopCheck == 1: #user wants to pick a loadout now too so it picks one for them
            pld = PickLoadout
            pld.shuffle() #shuffles the loadouts list 
            print("\n**********************************************************************************")
            pld.choose_loadout()
            print("\n**********************************************************************************")
        elif stopCheck ==2: #user does not want to pick a loadout and it ends the program
            stop = True
            print("\n Program finished good luck in the Outlands Legend")


elif rc == 3: #choice to start picking both a legend 
    plg = PickLegend
    plg.shuffle()
    print("\n**********************************************************************************")
    plg.choose_legend()
    pld = PickLoadout
    pld.shuffle()
    pld.choose_loadout()
    print("\n Program finished good luck in the Outlands Legend")
    print("\n**********************************************************************************")
    stop = False
    while not stop:
        stopCheck = int(input("\nWould you like to pick a another loadout or are you done? Enter 1 to pick another legend or 2 to stop: "))
        if stopCheck == 1: #user wants to pick a loadout now too so it picks one for them
            plg = PickLegend
            plg.shuffle()
            print("\n**********************************************************************************")
            plg.choose_legend()
            pld = PickLoadout
            pld.shuffle()
            pld.choose_loadout()
            print("\n Program finished good luck in the Outlands Legend")
            print("\n**********************************************************************************")
        elif stopCheck ==2: #user does not want to pick a loadout and it ends the program
            stop = True
            print("\n Program finished good luck in the Outlands Legend")

