# this is the main file where all the main logic is run

from datetime import *
# import json


StartTime = datetime.now(timezone.utc)

def main():
    while True:
        prompt = input("prompt: ")

        if prompt == "start":
            StartTime = datetime.now(timezone.utc)
            print("Started Timer At: " + str(StartTime))
        elif prompt == "stop":
            print("Stoped timer, you spent: " + str(datetime.now(timezone.utc) - StartTime) + "on that")
        elif prompt == "quit":
            break

if __name__ == "__main__":
    main()