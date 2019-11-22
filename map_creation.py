from request_lib import move, room_init

def create_map():
    print('##############################################')
    print('################ Creating Map ################')
    print('##############################################')

    # Basic stuff for traversal
    n_rooms = 500
    backtrack_stack = []
    visited = set()
    traversal_rooms = {}

    # Get starting room
    current_room = room_init()
    # create new room file and open the file object
    f = open("rooms.txt", "w")


    while len(visited) < n_rooms:
        # Get Current Room info
        current_room_id = current_room['room_id']
        current_room_title = current_room['title']
        current_room_desc = current_room['description']

        # If the current room is not in the set
        if current_room_id not in visited:
            # write the new room to the file
            f.write(f'{current_room}\n')
            # add it to the set
            visited.add(current_room_id)
            print(f'New Room! \n id:{current_room_id} \n name: {current_room_title}')
            print(f'Room Description: {current_room_desc}')
            print('##############################################')

        # If the room we are in doesn't exist on the graph yet, add exit objects!
        if current_room_id not in traversal_rooms:
            # Create all exits Object
            all_possible_exits = {}
            exits = current_room['exits']
            for exit in exits:
                all_possible_exits[exit] = "?"
            traversal_rooms[current_room_id] = all_possible_exits
        all_current_exits = traversal_rooms[current_room_id]

        ########### WET Traversal Code Based on Known Rooms ###########
        # Goin' North!
        if "n" in all_current_exits and all_current_exits["n"] == "?":
            # Move north
            new_room = move('n')
            new_room_id = new_room['room_id']
            traversal_rooms[current_room_id]['n'] = new_room_id
            # Add it to the graph if necessary
            if new_room_id not in traversal_rooms:
                new_room_exits = {}
                for exit in new_room['exits']:
                    new_room_exits[exit] = '?'
                new_room_exits['s'] = current_room_id
                traversal_rooms[new_room_id] = new_room_exits
            else:
                traversal_rooms[new_room_id]['s'] = current_room_id
            # Add to the backtrack stack
            backtrack_stack.append('s')
        
        # Goin' East!
        elif "e" in all_current_exits and all_current_exits["e"] == "?":
            # Move east
            new_room = move('e')
            new_room_id = new_room['room_id']
            traversal_rooms[current_room_id]['e'] = new_room_id
            # Add it to the graph if necessary
            if new_room_id not in traversal_rooms:
                new_room_exits = {}
                for exit in new_room['exits']:
                    new_room_exits[exit] = '?'
                new_room_exits['w'] = current_room_id
                traversal_rooms[new_room_id] = new_room_exits
            else:
                traversal_rooms[new_room_id]['w'] = current_room_id
            # Add to the backtrack stack
            backtrack_stack.append('w')

        # Goin' West!
        elif "w" in all_current_exits and all_current_exits["w"] == "?":
            # Move west
            new_room = move('w')
            new_room_id = new_room['room_id']
            traversal_rooms[current_room_id]['w'] = new_room_id
            # Add it to the graph if necessary
            if new_room_id not in traversal_rooms:
                new_room_exits = {}
                for exit in new_room['exits']:
                    new_room_exits[exit] = '?'
                new_room_exits['e'] = current_room_id
                traversal_rooms[new_room_id] = new_room_exits
            else:
                traversal_rooms[new_room_id]['e'] = current_room_id
            # Add to the backtrack stack
            backtrack_stack.append('e')

        # Goin' South!
        elif "s" in all_current_exits and all_current_exits["s"] == "?":
            # Move south
            new_room = move('s')
            new_room_id = new_room['room_id']
            traversal_rooms[current_room_id]['s'] = new_room_id
            # Add it to the graph if necessary
            if new_room_id not in traversal_rooms:
                new_room_exits = {}
                for exit in new_room['exits']:
                    new_room_exits[exit] = '?'
                new_room_exits['n'] = current_room_id
                traversal_rooms[new_room_id] = new_room_exits
            else:
                traversal_rooms[new_room_id]['n'] = current_room_id
            # Add to the backtrack stack
            backtrack_stack.append('n')

        ####### Out of options? Backtrack! #######
        else:
            # If we have no backtrack to do we will break the while loop
            if len(backtrack_stack) == 0:
                print(' \n\n\n\n\n\nend\n\n\n\n\n\n')
            # Else we backtrack
            else:
                # Pull the last element
                backtrack_path = backtrack_stack.pop()
                # Travel back to the backtrack travel path
                new_room = move(backtrack_path)
                print('############### Back Tracking! ###############')

        # replace room variables before returning to the top of the loop
        current_room = new_room
    
    f.close()
    f_2 = open('room_graph.txt', 'w')
    for key, value in traversal_rooms.items():
        f_2.write(f'{key}: {value}\n')
    f_2.close()

create_map()
