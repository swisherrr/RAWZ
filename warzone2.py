###########################################################################################
# Names: Zac Swisher,
# Date: 1/27
# Warzone Room ADventure with GUI
###########################################################################################
# import libraries
#from time import sleep
from tkinter import *


try:
    TAB_COMPLETE = True
    import TabCompleter as TC     # for tab completion (if available)
except ModuleNotFoundError:
    TAB_COMPLETE = False

###########################################################################################
# constants
VERBS = ["go", "look", "take"]  # the supported vocabulary verbs
QUIT_COMMANDS = ["exit", "quit", "bye"]  # the supported quit commands

###########################################################################################

# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, description, exits (e.g., south), exit locations (e.g., to the south is
        # room n), items (e.g., table), item descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self._name = name
        self._description = ""
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []
        self._enemies = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, value):
        self._image = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def enemies(self):
        return self._enemies

    @enemies.setter
    def enemies(self, value):
        self._enemies = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # add enemy to room
    def addEnemy(self, item):
        self._enemies.append(item)

    # returns a string description of the room as follows:
    def __str__(self):
        # first, the room name and description
        s = "{}\n".format(self._name)
        s += "{}\n".format(self._description)

        # next, the items in the room
        s += "You see: "
        for item in self._items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self._exits:
            s += exit + " "
        s += "\n"

        # next, the enemies in the room
        s += "Enemies: "
        for enemy in self._enemies:
            s += enemy + " "
        s += "\n"

        return s


###########################################################################################
# guns level
guns_list = {
    "knife": 1,
    "p890": 2,
    "x19": 2,
    "basp": 3,
    "m16": 3,
    "bryson800": 3,
    "vel46": 4,
    "fennec45": 4,
    "kastov74": 4,
    "lockwood": 5,
    "m4": 5,
    "signal50": 6,
    "airstrike": 7,
    "mortar_strike": 7
}


class Game(Frame):
    # constructor
    def __init(self, parent):
        # call constructor
        Frame.__init__(self, parent)
        
    # creates the rooms
    def createRooms():
        rooms = []

        # first, create the room instances so that they can be referenced below
        r1 = Room("Rohan Oil", "RO.png")
        r2 = Room("Taraq Village", "TV.png")
        r3 = Room("Al Mazrah City", "AMC.png")
        r4 = Room("Hydroelectric", "HE.png")
        r5 = Room("Marshlands", "ML.png")
        r6 = Room("Sa'id City", "SC.png")
        r7 = Room("Observatory", "OBVS.png")
        r8 = Room("Ahkdar Village", "AV.png")
        r9 = Room("Sarrif Bay", "SB.png")
        r10 = Room("Airport", "AP.png")
       # r11 = Room("Gulag")

        # room 1
        r1.description = "You landed in an oil refinery. Theres are no enemies here."
        r1.addExit("east", r2)
        r1.addExit("south", r4)
        r1.addItem("workbench", "There is a p890 on the top.")
        r1.addGrabbable("p890")
        Game.rooms.append(r1)

        # room 2
        r2.description = "You entered a small village on the outskirts of the map."
        r2.addExit("west", r1)
        r2.addExit("east", r3)
        r2.addEnemy("One enemy armed with a knife")
        r2.addItem("locker", "It is filled with old clothes and a basp smg.")
        r2.addGrabbable("basp")
        Game.rooms.append(r2)

        # room 3
        r3.description = "This is a big city will high rise towers."
        r3.addExit("west", r2)
        r3.addExit("south", r5)
        r3.addGrabbable("vel46")
        r3.addItem("opened_chests", "Someone got here before you.")
        r3.addItem("duffle_bag", "There is a vel46 in the bag.")
        Game.rooms.append(r3)

        # room 4
        r4.description = "You enter a small city along a river."
        r4.addExit("north", r1)
        r4.addExit("east", r5)
        r4.addExit("south", r7)
        r4.addEnemy("One enemy armed with a bryson800.")
        r4.addItem("safe", "Someone before you blew the safe open but left a m4 assault rifle inside.")
        r4.addGrabbable("m4")
        Game.rooms.append(r4)

        # room 5
        r5.description = "There isnt much cover. Most of the area is slightly flooded."
        r5.addExit("west", r4)
        r5.addExit("north", r3)
        r5.addEnemy("One enemy with a mortar_strike on standby.")
        Game.rooms.append(r5)

        # room 6
        r6.description = "The city is condensed and requires a keycard to access."
        r6.addExit("east", r7)
        Game.rooms.append(r6)

        # room 7
        r7.description = "You ventured up a tall mountain to reach this small town."
        r7.addExit("north", r4)
        r7.addExit("south", r8)
        r7.addExit("west", r6)
        r7.addItem("cabinet", "The cabinet is barren.")
       # r7.addEnemy("One enemy armed with a vel46.")
        Game.rooms.append(r7)

        # room 8
        r8.description = "You arrive at a small village at the base of the mountain."
        r8.addExit("south", r9)
        r8.addExit("north", r7)
        r8.addEnemy("One enemy armed with a bryson800.")
        r8.addItem("counter", "The counter is abnormally clean")
        Game.rooms.append(r8)

        # room 9
        r9.description = "You come accross a small city on the coast used as a port"
        r9.addExit("east", r10)
        r9.addExit("north", r8)
        r9.addItem("bed", "You look under the bed and find a keycard")
        r9.addItem("desk", "there is a signal50 sniper rifle leaning against the desk")
        r9.addGrabbable("signal50")
        r9.addGrabbable("keycard")
        # r9.addEnemy("One enemy with a fennec45 smg.")
        Game.rooms.append(r9)

        # room 10
        r10.description = "You arrive at a small abandoned airport."
        r10.addExit("west", r9)
        r10.addEnemy("One enemy with a precision airstrike on standby.")
        Game.rooms.append(r10)

        # set starting room
        currentRoom = r1

        return rooms, currentRoom
    # set up GUI
    def setupGUI(self):
        # organize GUI
        self.pack(fill=BOTH, expand=1)
        
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.bind("<Tab>", self.complete)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        img = None
        text_frame = Frame(self, width=WIDTH // 2)
        Game.image.image = img 
        Game.text = Text(text_frame, bg="lightgray", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)
        
    # set the current room image on the left of the GUI
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the right image
            Game.img = PhotoImage(file="skull.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game .currentRoom.image)
            
        # display the image on the left of GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img
        
    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text weidget, clear it, set it, and disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            #if dead, tell player
            Game.text.insert(END, "You are dead. The only thing you can do now\nis quit.\n")
        else:
            # otherwise, display appropriate status
            Game.text.insert(END, "{}\n\n{}\nYou are carrying: {}\n\n".format(status, Game.currentRoom, Game.inventory))
        Game.text.config(state=DISABLED)
        
        # support for tab completion
        if (Game.currentRoom != None):
            Game.words = VERBS + QUIT_COMMANDS + Game.inventory + Game.currentRoom.exits + Game.currentRoom.items + Game.currentRoom.grabbables
            
    
    # play game
    def play(self):
        # create rooms
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the initial status
        self.setStatus("WARZONE 2")
        
    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to compare the verb and noun to known values
        action = action.lower().strip()

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action in QUIT_COMMANDS):
            exit(0)

        # if the current room is None, then the player is dead
        # this only happens if the player goes south when in room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return
        
            
        
        
        


    ###########################################################################################
    # displays an appropriate "message" when the player "dies"
    # learned from https://www.youtube.com/watch?v=arcFqEuV_XQ
    def death():
        died = ("""
    ____    ____  ______    __    __      _______   __   _______  _______  
    \   \  /   / /  __  \  |  |  |  |    |       \ |  | |   ____||       \ 
     \   \/   / |  |  |  | |  |  |  |    |  .--.  ||  | |  |__   |  .--.  |
      \_    _/  |  |  |  | |  |  |  |    |  |  |  ||  | |   __|  |  |  |  |
        |  |    |  `--'  | |  `--'  |    |  '--'  ||  | |  |____ |  '--'  |
        |__|     \______/   \______/     |_______/ |__| |_______||_______/
        """)
        print("=" * 80)
        print(died)
        print("=" * 80)


    ###########################################################################################
    # check if the enemy inside the room has a better gun not
    # if yes, the function returns true which results in player's death
    def check_gun_levels(enemies, player_inventory):
        # set default highest level guns for enemy and player
        enemy_highest_level = 0
        player_highest_level = 0
        # normalize the decription of each enemy, learned from https://www.programiz.com/python-programming/methods/string/replace 
        for enemy in enemies:
            enemy = enemy.replace('.', '').replace(',', '').split()
            # for each word in description of enemy, check if the word is in the list of guns
            for word in enemy:
                if word in guns_list:
                    # set the level of gun for enemy
                    if enemy_highest_level < guns_list[word]:
                        enemy_highest_level = guns_list[word]
                        # for each item in player's inventory, check if the item is in the list of guns
        for item in player_inventory:
            if item in guns_list:
                # set the level of gun for enemy
                if player_highest_level < guns_list[item]:
                    player_highest_level = guns_list[item]
        # if enemy has higher level of gun, player dies and the game ends
        if enemy_highest_level > player_highest_level:
            print("Enemy has a better weapon than you do, he is killing you!")
            return True
        # if not, game continues
        else:
            return False

    # win function

    def win():
        win_message = ("""
    ____    ____  ______    __    __     ____    __    ____  ______   .__   __.  __  
    \   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / /  __  \  |  \ |  | |  | 
     \   \/   / |  |  |  | |  |  |  |     \   \/    \/   / |  |  |  | |   \|  | |  | 
      \_    _/  |  |  |  | |  |  |  |      \            /  |  |  |  | |  . `  | |  | 
        |  |    |  `--'  | |  `--'  |       \    /\    /   |  `--'  | |  |\   | |__| 
        |__|     \______/   \______/         \__/  \__/     \______/  |__| \__| (__) 

    """)
        print(win_message)

        

    ###########################################################################################
    # MAIN

    # support for tab completion
    if (TAB_COMPLETE):
        TC.parse_and_bind("tab: complete")

    # START THE GAME!!!
    inventory = []  # nothing in inventory...yet
    rooms, currentRoom = createRooms()  # add the rooms to the game

    # an introduction
    warzone = ("""
    ____    __    ____  ___      .______      ________    ______   .__   __.  _______ 
    \   \  /  \  /   / /   \     |   _  \    |       /   /  __  \  |  \ |  | |   ____|
     \   \/    \/   / /  ^  \    |  |_)  |   `---/  /   |  |  |  | |   \|  | |  |__   
      \            / /  /_\  \   |      /       /  /    |  |  |  | |  . `  | |   __|  
       \    /\    / /  _____  \  |  |\  \----. /  /----.|  `--'  | |  |\   | |  |____ 
        \__/  \__/ /__/     \__\ | _| `._____|/________| \______/  |__| \__| |_______|
    """)
    print(warzone)
    print("=" * 80)
    print("Objective: Get to the extraction point in Sa'id City.")
    # play forever (well, at least until the player dies or asks to quit)
    while (True):
        # while the player is alive, check if player killed enemy
        check_if_enemy_killed_player = check_gun_levels(currentRoom.enemies, player_inventory=inventory)
        if not check_if_enemy_killed_player:
            #if player killed the enemy, remove the enemy from the room and tell the player that they killed the enemy
            if len(currentRoom.enemies) != 0:
                print("\nYou killed the enemies in", currentRoom.name)
                currentRoom.enemies.clear()
        # set the status so the player has situational awareness
        # the status has room and inventory information
        status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

        # if the current room is None, then the player is dead
        # exit the game
        if (currentRoom == None):
            death()
            break
        # win condition
        if (currentRoom.name == "Sa'id City"):
            win()
            break

        # display the status
        print("=" * 80)
        print(status)

        if check_if_enemy_killed_player:
            death()
            break
        else:
            currentRoom.enemies = []
        # prompt for player input
        # the game supports a simple language of <verb> <noun>
        # valid verbs are go, look, and take
        # valid nouns depend on the verb
        action = input("What would you like to do? ")

        # set the user's input to lowercase to make it easier to compare the verb and noun to known values
        action = action.lower().strip()

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action in QUIT_COMMANDS):
            break
        
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs\nare {}.".format(", ".join(VERBS))
        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0].strip()
            noun = words[1].strip()

            # we need a valid verb
            if (verb in VERBS):
                # the verb is: go
                if (verb == "go"):
                    # set a default response
                    response = "You can't go in that direction."

                    # check if the noun is a valid exit
                    if (noun in currentRoom.exits):
                        if(currentRoom.name == "Observatory" and noun == "west" and not "keycard" in inventory):
                            response = "You cannot access this room without a keycard."
                        else:
                        # get its index
                            i = currentRoom.exits.index(noun)
                        # change the current room to the one that is associated with the specified exit
                            currentRoom = currentRoom.exitLocations[i]
                        # set the response (success)
                            response = "You walk {} and enter another room.".format(noun)
                        # the verb is: look
                elif (verb == "look"):
                    # set a default response
                    response = "You don't see that item."

                    # check if the noun is a valid item
                    if (noun in currentRoom.items):
                        # get its index
                        i = currentRoom.items.index(noun)
                        # set the response to the item's description
                        response = currentRoom.itemDescriptions[i]
                # the verb is: take
                elif (verb == "take"):
                    # set a default response
                    response = "You don't see that item."

                    # check if the noun is a valid grabbable and is also not already in inventory
                    if (noun in currentRoom.grabbables and noun not in inventory):
                        # room 1
                        if (currentRoom.name == "Rohan Oil" and noun == "p890"):
                            item_index = currentRoom.items.index("workbench")
                            currentRoom.itemDescriptions[item_index] = "There is nothing on the workbench."
                            # room 2
                        elif (currentRoom.name == "Taraq Village" and noun == "basp"):
                            item_index = currentRoom.items.index("locker")
                            currentRoom.itemDescriptions[item_index] = "There is old clothes in the locker."
                            # room 3
                        elif (currentRoom.name == "Al Mazrah City" and noun == "vel46"):
                            item_index = currentRoom.items.index("duffle_bag")
                            currentRoom.itemDescriptions[item_index] = "It is empty."
                            # room 4
                        elif (currentRoom.name == "Hydroelectric" and noun == "m4"):
                            item_index = currentRoom.items.index("safe")
                            currentRoom.itemDescriptions[item_index] = "There is nothing else in the safe."
                            # room 9
                        elif (currentRoom.name == "Sarrif Bay" and noun == "keycard"):
                            item_index = currentRoom.items.index("bed")
                            currentRoom.itemDescriptions[
                                item_index] = "You already checked under the bed. Are you scared of monsters?"
                        elif (currentRoom.name == "Sarrif Bay" and noun == "signal50"):
                            item_index = currentRoom.items.index("desk")
                            currentRoom.itemDescriptions[item_index] = "There are only papers on the desk."

                            # get its index
                        i = currentRoom.grabbables.index(noun)
                        # add the grabbable item to the player's inventory
                        inventory.append(currentRoom.grabbables[i])
                        # set the response (success)
                        response = "You take {}.".format(noun)

        # display the response
        if (currentRoom != None):
            print("=" * 80)
            print(response)

