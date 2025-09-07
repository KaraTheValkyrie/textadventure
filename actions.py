from classes import *

def look(object):
    if object == "self":
        status()
    else:   
        print(f"You are looking at {object}.")

def take(item):
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
    #"i": player.getinv,
    #"inv": player.getinv,
    #"items": player.getinv,
    "go": move,
    "move": move,
    "walk": move,
    "use": use,
    "mix": mix, 
    "combine": mix, 
    "status": status
}