from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Queue, Stack
from graph import Graph

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

qq = Queue()
st = Stack()

st.push([player.current_room])
qq.enqueue([player.current_room])
visited = set()
# print(st.stack)
# test = st.pop()
# print(test)
while len(world.rooms) != len(visited):
    path = st.pop()
    vertex = path[-1]    
    if vertex not in visited:
        visited.add(vertex)
        direction = random.choice(player.current_room.get_exits())
        next_room = player.current_room.get_room_in_direction(direction)
        if next_room in visited:
            st.push([player.current_room])
        else:
            player.travel(direction)
            traversal_path.append(direction)
            st.push([player.current_room])
    else:
        direction = random.choice(vertex.get_exits())
        player.travel(direction)
        traversal_path.append(direction)
        st.push([player.current_room])
    # path_a = st.pop()
    # path_b = qq.dequeue()
    # vertex_a = path_a[-1]
    # vertex_b = path_b[-1]
    # if vertex_a not in visited:
    #     visited.add(vertex_a)
    #     direction = random.choice(player.current_room.get_exits())
    #     next_room = player.current_room.get_room_in_direction(direction)
    #     if next_room in visited:
    #         st.push([player.current_room])
    #     else:
    #         player.travel(direction)
    #         traversal_path.append(direction)
    #         st.push([player.current_room])
    # elif vertex_a in visited:
    #     direction = random.choice(vertex_a.get_exits())
    #     next_room = player.current_room.get_room_in_direction(direction)
    #     if next_room in visited:
    #         st.push([player.current_room])
    #     else:
    #         player.travel(direction)
    #         traversal_path.append(direction)
    #         st.push([player.current_room])

    # if vertex_b not in visited:
    #     visited.add(vertex_b)
    #     direction = random.choice(player.current_room.get_exits())
    #     next_room = player.current_room.get_room_in_direction(direction)
    #     if next_room in visited:
    #         qq.enqueue([player.current_room])
    #     else:
    #         player.travel(direction)
    #         traversal_path.append(direction)
    #         qq.enqueue([player.current_room])
    # elif vertex_b in visited:
    #     direction = random.choice(vertex_b.get_exits())
    #     next_room = player.current_room.get_room_in_direction(direction)
    #     if next_room in visited:
    #         qq.enqueue([player.current_room])
    #     else:
    #         player.travel(direction)
    #         traversal_path.append(direction)
    #         qq.enqueue([player.current_room])
    











    # if vertex not in visited:
    #     visited.add(vertex)
    #     direction = random.choice(player.current_room.get_exits())
    #     next_room = player.travel(direction)
    #     if next_room in visited:
    #         pass
    #     else:
    #         player.travel(direction)
    #         traversal_path.append(direction)
    #         st.push([player.current_room])
    # else:
    #     direction = random.choice(vertex.get_exits())
    #     player.travel(direction)
    #     traversal_path.append(direction)
    #     st.push([player.current_room])

# player_room = player.current_room
# print('id',player_room.id)
# print(f'exits of room {player_room.id}', player_room.get_exits())
# cat = random.choice(player_room.get_exits())
# player.travel(cat)
# player_room = player.current_room
# print('id',player_room.id)
# print(f'exits of room {player_room.id}', player_room.get_exits())
# traversal_path.append(cat)

# qq.enqueue([player.current_room])
# st.push([player.current_room])
# while len(world.rooms) != len(visited):
#     path = qq.dequeue()
#     vertex = path[-1]
#     if vertex not in visited:
#         visited.append(vertex)
#         room = random.choice(vertex.get_exits())
#         if vertex.get_room_in_direction(room) not in visited:
#             player.travel(room)
#             traversal_path.append(player.travel(room))
#             print(player.current_room)
    # else:
    #     room = random.choice(vertex.get_exits())
    #     player.travel(room)
    #     traversal_path.append(player.travel(room))
    #     qq.enqueue([player.current_room])
    
# qq.enqueue([player.current_room])
# curroom = player.current_room.get_exits()
# visited = set()
# while qq.size() > 0:
#     path = qq.dequeue()
#     vertex = path[-1]
#     print('vertex',vertex)
#     if vertex not in visited:
#         visited.add(vertex)
#         traversal_path.append(vertex)
#         for exit_path in curroom:
#             room = random.choice(player.current_room.get_exits())
#             player.travel(room)
#             new_path = list(path)
#             new_path.append(exit_path)
#             qq.enqueue(exit_path)

# while qq.size() > 0:
#     #build a dictionary of exits of which room is connected to each room
#     #look for the most efficient path of each room
#     print('current room', player.current_room)
#     path = qq.dequeue()
#     vertex = path[-1]
#     print('vertex', vertex)
#     if vertex not in visited:
#         visited.add(vertex)
#         for room_exit in player.current_room.get_exits():
#             print('exit', room_exit)
#             player.travel(room_exit)
#             new_path = list(path)
#             new_path.append(room_exit)
#             qq.enqueue(room_exit)
# traversed_rooms = []
# traversed_rooms.append(player.current_room)

# print(player.current_room)
# print(player.current_room.get_exits())
    

# print('t path', traversal_path)


# TRAVERSAL TEST
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
