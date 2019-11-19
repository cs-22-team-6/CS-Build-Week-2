from world_creation import World_Creation

import ast
# read file
r = open('room_graph.txt', 'r')
contents = r.read()
r.close()
#create a list
room_list = contents.split('\n')
#remove the junk at the end
room_list.pop()
#fix my terrible formatting
room_list = ['{' + room + '}' for room in room_list]
# get list of dictionaries
room_graph = [ast.literal_eval(room) for room in room_list]
r = open('rooms.txt', 'r')
contents = r.read()
r.close()
# create a list
room_list = contents.split('\n')
# remove the junk at the end
room_list.pop()
# get list of room metadata
room_list = [ast.literal_eval(room) for room in room_list]
# get coords
titles = [room['coordinates'] for room in room_list]
# room coordinate dictionary
room_coord_dict = {room['room_id']: ast.literal_eval(room['coordinates']) for room in room_list}
# list of dict keys
key_list = list(room_coord_dict.keys())
final = {}
for i in range(len(room_graph)):
    final.update({key_list[i]: [room_coord_dict[key_list[i]], room_graph[i][key_list[i]]]})

world = World_Creation()

# roomGraph={
#     0: [(3, 5), {'n': 1}],
#     1: [(3, 6), {'s': 0, 'n': 2}],
#     2: [(3, 7), {'s': 1}]
# }

# roomGraph={
#     'room_id': 411,
#     'title': 'A misty room',
#     'description': 'You are standing on grass and surrounded by a dense mist. You can barely make out the exits in any direction.',
#     'coordinates': '(59,69)',
#     'elevation': 0,
#     'terrain': 'NORMAL',
#     'players': [],
#     'items': [],
#     'exits': ['w'],
#     'cooldown': 1.0,
#     'errors': [],
#     'messages': []
# }

world.loadGraph(final)
world.printRooms()