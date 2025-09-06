from text_parse import text_parse

def main():
    #run the main game loop
    while True:
        if text_parse(input("> ")) == "quit":
            return

main()