from actions import *

def text_parse(text):

    #first, check whether the input is one word or multiple
    #if it's one, it becomes a tuple with None as the second
    #item
    #if there's multiple words, then the string is split and put
    #into a tuple of words
    #this is necessary because we need to know whether we're passing
    #an argument to the command to run
    #some commands like "look" and "status" either don't accept any 
    if " " in text:
        input = tuple(text.split(maxsplit=1))
    else:
        input = (text, None)

    #check to see if the first word is in the action dictionary
    #and if it is, then run the associated command using the rest of
    #the input string as arguments for it
    if input[0] in actions_dict:
        if input[0] != "use":
            actions_dict[input[0]](input[1])

    #the quit command is special and has to be handled in a 
    #special way
    if input[0] == "quit":
        quit()

