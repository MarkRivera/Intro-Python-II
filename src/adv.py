from room import Room
from textwrap import TextWrapper

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
class Player:
    def __init__(self, name, location = room["outside"]):
        self.name = name
        self.location = location

    def where(self):
        print(f"{self.location.name}")

Player_1 = Player("Mark", room["outside"])
## Player_1.location = Player_1.location.n_to
Player_1.where()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def formatRoomDesc(description):
    textwrapper = TextWrapper(50)
    formatted_text = textwrapper.wrap(description)
    return [print(text) for text in formatted_text]

def movePlayer():
    print(Player_1.location.name)
    # Waiting For User Input
    userInput = input("Choose a direction (N, E, W, or S) to walk in... \n").lower()

    if userInput == "n":
        try:
            Player_1.location = Player_1.location.n_to
        except AttributeError:
            print("You find that you cannot move any further North")
        
    elif userInput == "e":
        try:
            Player_1.location = Player_1.location.e_to
        except AttributeError:
            print("You find that you cannot move any further East")
    
    elif userInput == "w":
        try:
            Player_1.location = Player_1.location.w_to
        except AttributeError:
            print("You find that you cannot move any further West")

    elif userInput == "s":
        try:
            Player_1.location = Player_1.location.s_to
        except AttributeError:
            print("You find that you cannot move any further South")
    
    elif userInput == "q":
        exit()

    else:
        return "Invalid option, please choose a cardinal direction (N, E, W, S) or quit (Q)"

    return

def game_loop():
    formatRoomDesc(Player_1.location.desc)
    movePlayer()
    game_loop()

game_loop()