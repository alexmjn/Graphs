"""This module implements full traversal of the Adventure Maps."""
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from os.path import dirname, join, realpath

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

world = World()

# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = join(dirname(realpath(__file__)),"maps/main_maze.txt")

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

#world.print_rooms()

player = Player(world.starting_room)

def traverse_maze(player):
    """Traverses the maze from the world defined in the adventure module.

    Uses a depth-first search to traverse a text map file and log the rooms'
    directional relationships (as can be conceptualized as nodes/edges on a
    graph). The current function traverses our main maze in 992 steps.

    This function depends on the Room, World, and Player classes defined
    in those respective modules. A World class object must be instantiated
    with a starting room from the Room class, then that world and starting
    room must be passed as an argument to a Player object. This function
    takes this Player as an argument and returns a dictionary of each room's
    valid exits.

    Note that a room_graph (as loaded in the code above) must also be accessible
    in this function's scope.
    """
    # set up our data structures for starting location and progress
    reverse_direction = {'s': 'n', 'n': 's', 'e': 'w', 'w': 'e'}
    traversal_path = []
    visited_rooms = set()
    s = Stack()
    current_room = player.current_room

    # Loop as long as we haven't visited all rooms.
    while len(visited_rooms) < len(room_graph):
        if current_room.id not in visited_rooms:
            visited_rooms.add(current_room.id)
        last_room = current_room

        for direction in current_room.get_exits():
            if current_room.get_room_in_direction(direction).id not in visited_rooms:
                # Add the opposite direction to the stack so we can go back.
                s.push(reverse_direction[direction])

                player.travel(direction)
                traversal_path.append(direction)
                visited_rooms.add(player.current_room.id)
                current_room = player.current_room
                break

        # If we're back where we started, retrace our steps.
        if last_room == current_room:
            direction = s.pop()
            player.travel(direction)
            traversal_path.append(direction)
            current_room = player.current_room

    return traversal_path

traversal_path = traverse_maze(player)

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
