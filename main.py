# this is the main file where all the main logic is run

from datetime import *
# import json


def main():
    StartTime = datetime.now(timezone.utc) # i hate python
    timing = False
    Currentboard = "NoBoard.json"

    while True:
        prompt = input(f"{Currentboard.split(".")[0]}: ")

        if prompt == "start":
            if (timing == False):
                StartTime = datetime.now(timezone.utc)
                timing = True
                print("Started Timer At: " + str(StartTime))
            else:
                print("you where already timing somthing, you must stop it to start another") # we should make it so that you can run multible at once somt time in the future

        elif prompt == "stop":
            if timing:
                print("Stoped timer, you spent: " + str(datetime.now(timezone.utc) - StartTime) + "on that")
                timing = False
                # save the time chunk to memory or somthing
            else:
                print("you where not timing anything")
        
        elif prompt == "new board":
            NewBoardName = input("what should the board be called? ") + ".json"
            try:
                with open(NewBoardName, "r") as file:
                    if input("that file already exists, would you like to open it? ") == "yes":
                        Currentboard = NewBoardName
            except FileNotFoundError:
                with open(NewBoardName, "w"):
                    pass
            Currentboard = NewBoardName

        elif prompt == "quit":
            break

if __name__ == "__main__":
    main()