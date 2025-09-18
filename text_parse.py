from actions import *

def text_parse(text):

    #first, check whether the input is one word or multiple
    #if it's one, it becomes a tuple with None as the second item
    #if there's multiple words, then the string is split and put into a tuple of words
    #this is necessary because we need to know whether we're passing an argument to the command to run
    #some commands like "look" and "status" either don't accept 
    if " " in text:
        text_input = tuple(text.split(maxsplit=1))
    else:
        text_input = (text, None)

    #the quit command is special and has to be handled in a 
    #special way
    if text_input[0] in ("q", "quit"):
        if input("Are you sure? (y/n)\n") in ("y", "yes"):
            quit()
        else:
            return

    #check to see if the first word is in the action dictionary
    #and if it is, then run the associated command using the rest of
    #the input string as arguments for it
    if text_input[0] in actions_dict:
        actions_dict[text_input[0]](text_input[1])
    else:
        print(ERR_INVALID_ACTION)

