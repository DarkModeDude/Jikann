# this is the main file where all the main logic is run

from datetime import *
from json import load, dump


# check to see if a board exists in the current directory:
def DoesBoardExist(BoardName=""):
    try:
        file = open(BoardName, "r")
        file.close()
        return True
    except FileNotFoundError:
        return False

# get the name of a board from the user:
def GetBoardName(prompt="board name? "):
    return input(prompt).split('.')[0] + ".json"

# create a board file:
def CreateBoard(BoardName=""):
    with open(BoardName, "w"):
        pass

def LoadBoard(BoardName):
    with open(BoardName, "r") as board:
        return load(board)

def WriteBoard(BoardName, data):
    with open(BoardName, "w") as board:
        dump(data, board)


def main():
    # multi prompt loop variables:
    data = {}
    StartTime = datetime.now(timezone.utc)
    timing = False
    Currentboard = "NoBoard.json"

    # prompt loop:
    while True:
        prompt = input(f"{Currentboard.split(".")[0]}: ") # get the current command

        # starting a timer:
        if prompt == "start":
            if (timing == False):
                StartTime = datetime.now(timezone.utc)
                timing = True
                print("Started Timer At: " + str(StartTime))
            else:
                print("you where already timing somthing, you must stop it to start another")
                # we should make it so that you can run multible at once somt time in the future

        # stoping a timer:
        elif prompt == "stop":
            if timing:
                print("Stoped timer, you spent: " + str(datetime.now(timezone.utc) - StartTime) + "on that")
                timing = False
                WriteBoard(Currentboard, data)
            else:
                print("you where not timing anything")
        
        # createing a new time board:
        elif prompt == "new board" or prompt == "new":
            NewBoardName = GetBoardName("what should the board be called? ")
            if DoesBoardExist(NewBoardName):
                if input("that file already exists, would you like to open it? ") == "yes":
                    Currentboard = NewBoardName
            else:
                CreateBoard(NewBoardName)
                Currentboard = NewBoardName
        
        # loading a differnt board:
        elif prompt == "load board" or prompt == "load":
            LoadingBoard = GetBoardName("what is the new baord name? ")
            if DoesBoardExist(LoadingBoard):
                Currentboard = LoadingBoard
                data = LoadBoard(Currentboard)
                print("board loaded")
            else:
                print("that board does not exist in the current directory")

        elif prompt == "save":
            WriteBoard(Currentboard, data)

        # quiting the program:
        elif prompt == "quit":
            break
        print(data)

if __name__ == "__main__":
    main()