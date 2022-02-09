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
        
        print(f"\nFirst Choice (MUST USE THIS IF AVAILABLE: {firstChoice} \n Second Choice (Only use if 1st option is not available): {secondaryChoice} \n Third Choice (ONLY USE IF first 2 choices ARE NOT AVAILABLE): {lastChoice}")
        

class PickLoadout:
    global loadout
    loadout = ["Havoc Rifle", "VK-47 Flatline", "Hemlok Burst AR", "R-301 Carbine", "Alternator SMG", "Prowler Burst PDW", "R-99", "Volt SMG", "C.A.R. SMG", "Devotion LMG", "L-Star EMG", "M600 Spitfire", "Rampage LMG", "G7 Scout", "Triple Take", "30-30 Repeater", "Bocek Compund Bow", "Charge Rifle", "Longbow DMR", "Kraber .50-Cal Sniper", "Sentinel","EVA-8 Auto", "Mastiff Shotgun", "Mozambique Shotgun", "Peacekeaper", "RE-45", "P2020", "Wingman"] # a list of all current guns in apex legends, may need to be updated in the future 

    def shuffle():
        for i in range(len(loadout)-1, 0, -1):
            #pick a random index from 0 to i 
            j = random.randint(0, i +1)
            #swap arr[i] with the element at random index 
            loadout[i], loadout[j] = loadout[j], loadout[i]
            
    def choose_loadout():
        primaryGun = loadout[0] #displays gun at index 0 in the loadout list
        secondaryGun = loadout[1] #displays gun at index 1 in the loaoduts list
        backupGun = loadout[2] #displays gun at index 2 in the loadouts

        print(f"\n Primary Gun: {primaryGun} \n Secondary Gun: {secondaryGun}\n Backup Gun (Only if one of the first two are CP guns): {backupGun}\n")

plg = PickLegend
plg.shuffle()
plg.choose_legend()
pld = PickLoadout           
pld.shuffle()
pld.choose_loadout()
