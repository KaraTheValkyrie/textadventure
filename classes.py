from dataclasses import dataclass

class Player:
    def __init__(self):
        self.inventory = []
        self.flags = {}
    
    def getinv(self):
        if len(self.inventory) == 0:
            print("You don't have any items.")
            return None
        
        print("Your inventory contains the following:")
        for item in self.inventory:
            print(item.name_long)

@dataclass
class Room:
    name: str
    desc: str
    doors: list
    objects: list
    items: list

@dataclass
class Object:
    name: str
    desc: str
        
@dataclass        
class Item:
    name_short: str
    name_long: str
    desc: str
    combine_actions: dict
    use_actions: dict
    
