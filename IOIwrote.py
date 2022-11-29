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

def ReadStr(qstStr:str="", validStr=['y','Y','n','N'])->str:

    if validStr is None:
        validStr = ['y', 'Y', 'n', 'N']
    valid:bool=False
    userInput:str=""

    while valid==False:

        userInput=input(qstStr)

        if userInput in validStr:
            valid=True

        else:
            print("Invalid input!")

    return userInput

def YNDecision(decisionStr:str="")->bool:

    userInput:str='n'

    userInput=ReadStr(qstStr=decisionStr)

    if userInput in ['y','Y']:
        return True

    else:
        return False

if __name__ == "__main__":

    while True:
        userInput = ReadInt("int Input: ")
        print("User's int inputed: ", userInput)
        userInput = ReadFloat("float Input: ")
        print("User's float inputed: ", userInput)

    input()