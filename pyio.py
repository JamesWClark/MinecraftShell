from mcpi.minecraft import Minecraft

mc = Minecraft.create()

'''
HOME
'''

# displays the home menu
def home():
    print("What would you like to do?")
    print("1 - Save Checkpoint")
    print("2 - Restore Checkpoint")
    print("3 - Terraform")
    print("4 - Navigate")
    print("5 - Build")
    choice = input("Hmm? ")
    routeDecisions('Home', choice)

# saves a checkpoint
def home1():
    mc.saveCheckpoint()
    print("Checkpoint Saved")
    home()

# restores the last checkpoint
def home2():
    mc.restoreCheckpoint()
    print("Checkpoint Restored")
    home()

'''
TERRAFORM
'''

# displays the terraforming menu
def terraform():
    print("How do you want to terraform?")
    print("1 - Turn everything to air")
    print("2 - Build a random layered ground")
    print("C - Cancel")
    choice = input("Hmm? ")
    routeDecisions('Terraform', choice)

# turns every block to air
def terraform1():
    mc.setBlocks(-127,-126,-127, 127, 127, 127, 0)

'''
NAVIGATE
'''

# displays the navigation menu
def navigate():
    print("Where do you want to go?")
    print("1 - Teleport")
    print("C - Cancel")
    choice = input("Hmm? ")
    routeDecisions('Navigate', choice)

# teleports the player
def navigate1():
    x, y, z = getLocation()
    mc.player.setPos(x, y, z)
    print("Teleporting to {0},{1},{2}".format(x,y,z))

'''
BUILD
'''

# displays the build menu
def build():
    print("What do you want to build?")
    print("1 - Empty Enclosure")
    print("2 - Tunnel")
    print("C - Cancel")
    choice = input("Hmm? ")
    routeDecisions('Build', choice)

def build1():
    w = int(input("How wide? "))
    h = int(input("How tall? "))
    l = int(input("How long? "))
    b = int(input("Which block? "))
    print("Where?")
    print("1 - My Location")
    print("2 - Another Location")
    choice = input("Hmm ?")
    x = None
    y = None
    z = None
    if choice == "1":
        x, y, z = mc.player.getPos()
    elif choice == "2":
        x, y, z = getLocation()

    x = int(x)
    y = int(y)
    z = int(z)

    mc.setBlocks(x,y,z,x+w,y+h,z+l,b)
    for i in range(x+1, x + w-1):
        for j in range(y+1, y + h-1):
            for k in range(z+1, z + l - 1):
                mc.setBlock(i, j, k, 0)
'''
UTILITY
'''

# returns an x, y, z tuple
def getLocation():
    x = int(input("X = ? "))
    y = int(input("Y = ? "))
    z = int(input("Z = ? "))
    return x, y, z

'''
ROUTE DECISIONS
'''

# routes all the programming decisions    
def routeDecisions(arrivingFrom, choice):
    if arrivingFrom == 'Home':        
        if choice == "1":
            home1()
        elif choice == "2":
            home2()
        elif choice == "3":
            terraform()
        elif choice == "4":
            navigate()
        elif choice == "5":
            build()
        else:
            home()
    elif arrivingFrom == 'Terraform':
        if choice == "1":
            terraform1()
        elif choice == "C":
            home()
        else:
            terraform()
    elif arrivingFrom == 'Navigate':
        if choice == "1":
            navigate1()
        elif choice == "C" or choice == "c":
            home()
        else:
            terraform()
    elif arrivingFrom == "Build":
        if choice == "1":
            build1()
        elif choice == "C" or choice == "c":
            home()
        else:
            build()

'''
BEGIN ACTUAL PROGRAM
'''

home()
            

