def ReadInt(qstStr:str="")->int:
    valid:bool=False
    userInput:int

    while valid==False:
        try:
            userInput=int(input(qstStr))
            valid=True
        except ValueError:
            print("Invalid input!")

    return userInput

def ReadFloat(qstStr:str="")->float:
    valid:bool=False
    userInput:float

    while valid==False:
        try:
            userInput=float(input(qstStr))
            valid=True
        except ValueError:
            print("Invalid input!")

    return userInput

if __name__ == "__main__":

    while True:
        userInput = ReadInt("int Input: ")
        print("User's int inputed: ", userInput)
        userInput = ReadFloat("float Input: ")
        print("User's float inputed: ", userInput)

    input()