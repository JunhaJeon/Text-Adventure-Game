def examine(objects, command):
    obj_name = command.split("examine", 1)[1].strip().lower()
    for obj in objects:
        if obj[0].lower() == obj_name:
            print(f"{obj[0]}: {obj[1]}")
            return
    print(f"There's nothing called '{obj_name}' here to examine.")

def parse_data(filename):
    rooms = []

    with open(filename, "r") as file:
        for line in file:
            if not line.strip() or line.startswith("#"):
                continue

            parts = [part.strip() for part in line.split(" | ")]
            label = parts[0]

            if label == 'Room':
                room = [parts[1], parts[2], [], []]  # name, desc, objects, exits
                rooms.append(room)

            elif label == 'Object':
                obj = (parts[1], parts[2], parts[3])
                for room in rooms:
                    if room[0] == obj[2]:
                        room[2].append(obj)
                        break

            elif label == 'Exit':
                from_room = parts[1]
                to_room = parts[2]
                desc = parts[3]
                direction = parts[4]

                from_index = next((i for i, room in enumerate(rooms) if room[0] == from_room), None)
                to_index = next((i for i, room in enumerate(rooms) if room[0] == to_room), None)

                if from_index is not None and to_index is not None:
                    rooms[from_index][3].append((to_index, direction, desc))

    return rooms

def describe_room(room):
    print(f"\nYou're currently at {room[0]}: {room[1]}")
    print(f"\nAvailable exits:")
    for exit_info in room[3]:
        print(f"    {exit_info[1]} (movement): {exit_info[2]}")
    if not room[2]:
        print(f"\nNo available objects in {room[0]}")
    else:
        print(f"\nAvailable objects in {room[0]}:")
        for obj in room[2]:
            print(f"    {obj[0]}")

def describe_room_brief(room):
    print(f"\nYou're currently at {room[0]}: {room[1]}")

def game_loop(rooms):
    print("Welcome to the sleepover at my uncle's luxurious mansion!")
    current_index = 0

    while True:
        current_room = rooms[current_index]
        describe_room(current_room)  # Show room on entry

        while True:
            command = input("\nWhat would you like to do? (You can move, 'look', 'examine <object>', or 'exit')\n> ").strip().lower()

            if command == "exit":
                print("Thanks for playing!")
                return

            elif command == "look":
                describe_room_brief(current_room)

            elif command.startswith("examine"):
                examine(current_room[2], command)
                # Don't re-describe the room here

            else:
                # Try movement
                for exit_info in current_room[3]:
                    if command == exit_info[1].lower():
                        current_index = exit_info[0]
                        break
                else:
                    print("Invalid command or direction. Try again.")
                    continue  # Stay in current room

                break  # Break to re-describe the new room

def main():
    rooms = parse_data("edited_data.txt")
    game_loop(rooms)

if __name__ == "__main__":
    main()
