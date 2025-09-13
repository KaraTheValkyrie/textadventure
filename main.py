from game_data import *
from text_parse import text_parse

#initialize the game


def main():
    #run the main game loop
    while True:
        text_parse(input("> "))

if __name__ == "__main__":
    main()