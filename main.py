from text_parse import text_parse
from game_data import *

#initialize the game
#first, create a player object

player = Player(PLAYER_STARTING_ROOM, [], PLAYER_FLAGS_DICT)

def main():
    #run the main game loop
    while True:
        text_parse(input("> "))

if __name__ == "__main__":
    main()