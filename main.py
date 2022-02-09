import random 

class PickLegend:
    global legends
    legends = ["Ash", "Bangalore", "Bloodhound", "Caustic", "Crypto", "Fuse", "Gibraltar", "Horizon", "Lifeline", "Loba", "Mad Maggie", "Mirage", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer","Valkyrie", "Wattson"]
    
    def shuffle():
        for i in range(len(legends)-1, 0, -1):
            #pick a random index from 0 to i 
            j = random.randint(0, i +1)
            #swap arr[i] with the element at random index 
            legends[i], legends[j] = legends[j], legends[i]
            
    def choose_legend():
        firstChoice = legends[0]
        del legends[0]
        secondaryChoice = legends[0]
        del legends[0]
        lastChoice = [0]
        del legends[0]
        print(f"First Choice (MUST USE THIS IF AVAILABLE")
        

class PickLoadout:
    global loadout
    loadout = ["Havoc Rifle", "VK-47 Flatline", "Hemlok Burst AR", "R-301 Carbine", "Alternator SMG", "Prowler Burst PDW", "R-99", "Volt SMG", "C.A.R. SMG", "Devotion LMG", "L-Star EMG", "M600 Spitfire", "Rampage LMG", "G7 Scout", "Triple Take", "30-30 Repeater", "Bocek Compund Bow", "Charge Rifle", "Longbow DMR", "Kraber .50-Cal Sniper", "Sentinel","EVA-8 Auto", "Mastiff Shotgun", "Mozambique Shotgun", "Peacekeaper", "RE-45", "P2020", "Wingman"]

    def shuffle():
        for i in range(len(legends)-1, 0, -1):
            #pick a random index from 0 to i 
            j = random.randint(0, i +1)
            #swap arr[i] with the element at random index 
            loadout[i], loadout[j] = loadout[j], loadout[i]
            
    def choose_loadout():
        primaryGun = loadout[0]
        del loadout[0]
        secondaryGun = loadout[0]
        del loadout[0]
        backupGun = loadout[0]
        del loadout[0]
        print(f" Primary Gun: {primaryGun} \n Secondary Gun: {secondaryGun}\n Backup Gun (Only if one of the first two are CP guns): {backupGun}")

plg = PickLegend()
plg.shuffle()        
pld = PickLoadout           
pld.shuffle()
pld.choose_loadout()
