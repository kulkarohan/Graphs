from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = room_graph

    def get_neighbors(self, room_id):
        return self.vertices[room_id][1]


def dft(starting_room):
    graph = Graph()
    room_stack = Stack()
    direction_stack = Stack()

    path = []
    visited = set()

    room_stack.push(starting_room)

    while room_stack.size() > 0:
        current_room = room_stack.pop()
        current_direction = direction_stack.pop()

        path.append(current_direction)

        if current_room not in visited:
            visited.add(current_room)

            edges = graph.get_neighbors(current_room)

            for direction in edges.keys():
                direction_stack.push(direction)

            for room in edges.values():
                room_stack.push(room)

    return [path, visited]

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# Initialize player
player = Player(world.starting_room)


player.current_room = world.starting_room

traversal_path = dft(player.current_room.id)[0]
visited_rooms = dft(player.current_room.id)[1]

for move in traversal_path:
    player.travel(move)

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
