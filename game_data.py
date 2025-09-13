from classes import *

hammer = Item(
    (
        "hammer",
        "sledgehammer",
        "mallet"
    ),
    "a sledgehammer",
    "This sledgehammer is made entirely of steel with a rubber grip. It looks very sturdy.",
    "A sledgehammer is leaning against the wall.",
    "This sledgehammer is made entirely of steel with a rubber grip. It looks very sturdy.",
    True,
    True,
    {}
)

id_card = Item(
    (
        "id card",
        "id",
        "keycard"
    ),
    "an ID card",
    "This bloodstained ID card has a picture of a scientist and the name Dr. John Doe on it.",
    "An ID card can be seen next to the corpse.",
    "This bloodstained ID card has a picture of a scientist and the name Dr. John Doe on it. It can be used to open doors.",
    True,
    False,
    {}
)

corpse = Object(
    (
        "corpse",
        "body",
        "dead body",
        "dead scientist"
    ),
    "This scientist has several lacerations across his chest. He seems to have been killed by a bladed weapon.",
    "The remains of a scientist can be seen on the floor in a pool of blood.",
    [id_card],
    {}
)

room1 = Room(
    (
        "room1",
        "room 1",
        "room one"
    ),
        "This is test room one.",
        [],
        [],
        [hammer]
)

PLAYER_STARTING_ROOM = room1
PLAYER_FLAGS_DICT = {
    "is_shackled": True,
    "is_robot": True
}

ERR_INVALID_ACTION = "Error: Invalid action."
ERR_TARGET_NOT_FOUND = "Error: Target object not found."

player = Player(PLAYER_STARTING_ROOM, [], PLAYER_FLAGS_DICT)