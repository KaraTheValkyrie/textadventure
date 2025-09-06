from actions import *

def text_parse(text):
    input = text.split()
    if input[0] in actions_dict:
        if input[0] != "use":
            actions_dict[input[0]](input[-1])

    if input[0] == "quit":
        return input[0]

