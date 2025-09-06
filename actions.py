def look(object):
    print(f"You are looking at {object}.")

def take(item):
    print(f"You take the {item}.")

def move(direction):
    print(f"You walk through the {direction} door.")

def use(item, target):
    print(f"You use the {item} on the {target}.")

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
    "use": use
}