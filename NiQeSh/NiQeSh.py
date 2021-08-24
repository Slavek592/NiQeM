#!/usr/bin/python3
import os
from Definitions import Runner
from Definitions import Files

print("Welcome, User!")
print("NiQeSh 'compiler' greets You!")
level = 0
while True:
    print("Level " + str(level))
    command = str(input("Input the name of Your file:\nname/stop "))
    if command in ["break", "Break", "stop", "Stop", "exit", "Exit", "quit", "Quit", "escape", "Escape"]:
        Runner.finish(level)
        print("OK")
        break
    elif command in ["empty", "Empty"]:
        Files.refresh_folder()
        print("OK")
        break
    else:
        if os.path.isfile(command):
            result = Runner.run_from_file(command, level)
        elif os.path.isfile(command + ".nqs"):
            result = Runner.run_from_file(command + ".nqs", level)
        elif os.path.isfile("NiqeshScripts/" + command):
            result = Runner.run_from_file("NiqeshScripts/" + command, level)
        elif os.path.isfile("NiqeshScripts/" + command + ".nqs"):
            result = Runner.run_from_file("NiqeshScripts/" + command + ".nqs", level)
        else:
            result = False
            print("It does not exist, I am sorry.")
        if result:
            level += 1
print("Thank You for using NiQeSh and NiQeM!")
print("Goodbye!")
