from dataclasses import dataclass

#areas the player can be in and that contain objects and items
@dataclass
class Room:
    #the name of the room, for use with move()
    name: tuple
    #the description of the room, given when the player enters
    #and when they use look() without any arguments
    desc: str
    #a list of doors to other rooms
    doors: list
    #a list of objects in the room
    objects: list
    #a list of items in the room
    items: list

    #this function checks if the target string matches the name of
    #any item, door, or object in the room, returning the target object
    #if found, and returning None otherwise
    def is_in_room(self, target):
        for it in self.items:
            for name in it.names:
                if name == target:
                    return it
        
        for obj in self.objects:
            for name in obj.names:
                if name == target:
                    return obj
        
        for d in self.doors:
            for name in d.names:
                if name == target:
                    return d
        
        return None
    
    #this function prints the room's description as well as the
    #desc_short for everything in the room
    def examine(self):
        pass

#objects in the environment that can be looked at, and maybe 
#interacted with, but not picked up
@dataclass
class Object: 
    #the list of names the player can use for the object
    names: tuple 
    #the description to show when the player uses look() on it
    desc: str
    #the description given in the room overview
    desc_short: str
    #the list of items that are contained within the object; look()
    #will reveal all of these items that have (visible=False)
    #if the items aren't supposed to be revealed, like an item in an
    #opaque lockbox, then don't use this and spawn them when it's open
    contains: list
    #this defines interactions when an item is used on the object
    use_actions: dict

#items in the environment that the player can look at, pick up,
#and either use on objects or combine with other items        
@dataclass        
class Item:
    #the list of names the player can use for the item
    names: tuple
    #the item's display name in the player's inventory
    name_long: str
    #the description to show when the player uses look() on it
    desc: str
    #the description given in the room overview
    desc_short: str
    #the description after it's been picked up and the player
    #uses look() on it
    desc_in_inv: str
    #False if the item is locked away or otherwise inaccessible
    #until the player takes a specific action, True if it can
    #immediately be taken
    available: bool
    #False if the item is hidden in some way, but looking at its
    #container reveals it; True if it isn't hidden and should
    #be included in the room's look() description
    visible: bool
    #this defines interactions the item has with other items
    combine_actions: dict

#these lead to other rooms and may be locked
@dataclass
class Door:
    #the list of names the player can use for the door
    names: tuple
    #the description to show when the player uses look() on it
    desc: str
    #the description given in the room overview
    desc_short: str
    #False if the door is locked or otherwise can't be opened,
    #True if the player can go through it
    usable: bool

#the player object
@dataclass
class Player:
    #the room the player is currently in
    location: Room
    #the player's inventory, represented as a list of items
    inventory: list
    #story flags the player has activated
    flags: dict    
    
    #this method prints the player's inventory
    def getinv(self):
        if len(self.inventory) == 0:
            print("You don't have any items.")
            return None
        
        print("Your inventory contains the following:")
        for item in self.inventory:
            print(item.name_long)
    
    #this method checks if the player has a specified item
    #and returns the item if found, or None if not found
    #this should only be used with strings, use 
    # if item in player.inventory 
    #with an item object
    def is_in_inv(self, target):
        for it in self.inventory:
            for name in it.names:
                if name == target:
                    return it
        
        return None