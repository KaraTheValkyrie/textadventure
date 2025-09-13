from classes import *

room1 = Room(
    (
        "room1",
        "room 1",
        "room one"),
        "This is test room one.",
        [],
        [],
        []
)

PLAYER_STARTING_ROOM = room1
PLAYER_FLAGS_DICT = {
    "is_shackled": True,
    "is_robot": True
}

player = Player(PLAYER_STARTING_ROOM, [], PLAYER_FLAGS_DICT)