command = ""
started = False
while command.lower() != "quit":
    command = input("> ").lower()
    if command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == "start":
        if started:
            print("car already started!")
        else:
            started = True
            print("car started... ready to go")
    elif command == "stop":
        if not started:
            print("car already stopped!")
        else:
            started = False
            print("car stopped")
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand")
