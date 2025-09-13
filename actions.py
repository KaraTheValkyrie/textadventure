from classes import *
from game_data import *

def look(target=None):
    #this command will describe everything in a room, or give
    #more detail about a specific thing in the room if an argument
    #is given

    #we need some if statements to figure out what to look at
    #if there was nothing specified, then check the current room

    if target == None:
        player.location.examine()
        return
    
    #check if the player typed "check self", "look self", etc.
    #this is handled by a separate command, so just call it instead
    if target == "self":
        status()
        return
    
    #check if the target is in the current room's object, item, or
    #door arrays, or the player's inventory, and if it is, print the 
    #desc for that thing
    target_object = player.location.is_in_room(target)
    if target_object == None:
        target_object = player.is_in_inv(target)

    if target_object != None:
        print(target_object.desc)
        #if the target is a container object, reveal all of the items
        #inside it and print them too
        if type(target_object) == Object:
            for it in target_object.contains:
                it.visible = True
                print(it.desc)
        return

    #if the target object still can't be found, print an error message
    print("Error: Target not found.")


def take(item):
    #if the input refers to an item that's visible, accessible, and in 
    #the current room, it adds the item to the player's inventory and
    #removes it from the room
    print(f"You take the {item}.")

def move(direction):
    print(f"You walk through the {direction} door.")

def use(item, target=None):
    print(f"You use the {item} on the {target}.")

def mix(item1, item2):
    print(f"You combine the {item1} with the {item2}.")

def status():
    print(f"Your systems are fully functional.")

actions_dict = {
    "look": look,
    "examine": look,
    "check": look,
    "take": take,
    "get": take,
    "pick": take,
    "i": player.getinv,
    "inv": player.getinv,
    "items": player.getinv,
    "go": move,
    "move": move,
    "walk": move,
    "use": use,
    "mix": mix, 
    "combine": mix, 
    "status": status
}