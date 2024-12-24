def examine(objs, command):
    obj_name = command.split("examine",1)[1].strip()
    for obj in objs:
        if(obj[0] == obj_name):
            print(f"{obj[0]}: {obj[1]}")
            break

def main():
    rooms_list = []
    f = open("edited_data.txt", "r")    

    # Iterate through each line
    for line in f:
        # Skip empty lines
        if not line.strip():
            continue

        # Split the line into words
        words = line.split(" | ")
        # Check the label (Room, Object, Exit)
        label = words[0]

        # Process the line based on the label
        if label == 'Room':
            room_name = words[1].strip()
            room_description = words[2].strip()
            current_room = [room_name, room_description, [], []]
            rooms_list.append(current_room)
        elif label == 'Object':
            # Extract object details
            object_name = words[1].strip()
            object_description = words[2].strip()
            object_location = words[3].strip()
            for room in rooms_list:
                if(object_location==room[0]):
                    room[2].append((object_name, object_description, object_location))
                    break
        elif label == 'Exit':
            # Extract exit details
            exit_from = words[1].strip()
            exit_to = words[2].strip()
            exit_description = words[3].strip()
            exit_direction = words[4].strip()
            for i in range(len(rooms_list)):
                if(exit_from==rooms_list[i][0]):
                    current_room_index = i
                if(exit_to==rooms_list[i][0]):
                    exit_room_index = i
            rooms_list[current_room_index][3].append((exit_room_index, exit_direction, exit_description))
    f.close()

    print("Welcome to the sleepover at my uncle's luxurious mansion!\n")
    is_exit = False
    current_room_index = 0
    while(not is_exit):
        current_room = rooms_list[current_room_index]
        print(f"You're currently at {current_room[0]}: {current_room[1]}")
        print(f"Here is a list of available exits for {current_room[0]}:")
        exit_directions = []
        for exit in current_room[3]:
            exit_room_index = exit[0]
            exit_directions.append(exit[1])
            print(f"    {exit[1]}(movement): {exit[2]}")
        if(len(current_room[2]) == 0):
            print(f"No available objects for {current_room[0]}")
        else:
            print(f"Here is a list of available objects for {current_room[0]}:")
            for obj in current_room[2]:
                print(f"    {obj[0]}")

        while(True):
            command = input("What would you like to do? (You can give a movement command or a command like 'look' or 'examine' or 'exit') ").strip()
            if(command == "exit"):
                is_exit = True
                break
            elif(command == "look"):
                print(f"{current_room[0]}: {current_room[1]}")
            elif("examine" in command):
                examine(current_room[2], command)
            elif(command in exit_directions):
                found = False
                for exit in current_room[3]:
                    if(exit[1] == command):
                        current_room_index = exit[0]
                        found = True
                        break
                if(found):
                    break
        print("")

main()