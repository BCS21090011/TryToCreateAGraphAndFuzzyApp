from matplotlib import pyplot as plt
import IOIwrote as IO
import os


if __name__=="__main__":

    xlim_l:float=None
    xlim_r:float=None
    ylim_d:float=None
    ylim_u:float=None
    xlabel:str=None
    ylabel:str=None
    title:str=None
    legLocIndex:int=1
    legLoc:list=['best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center']
    saveDir:str=""
    saveName:str=""
    absltName:str=""

    lnNum:int=IO.ReadInt("Number of lines: ")

    for i in range(lnNum):

        label:str=None
        x:list=[]
        y:list=[]

        print(f"Line {i:>3}:")
        pntNum:int=IO.ReadInt("Number of points: ")

        for j in range(pntNum):

            print(f"Coordinate {j:>3}:")
            xCoor:float=IO.ReadFloat("X coordinate: ")
            yCoor:float=IO.ReadFloat("Y coordinate: ")

            x.append(xCoor)
            y.append(yCoor)

        print("\n")

        if IO.YNDecision(decisionStr="With label? (Y/N)\n")==True:
            label=input(f"Label for line {i:>3}: ")

        plt.plot(x,y,label=label)

        print("\n\n")

    if IO.YNDecision(decisionStr="Custom x-axis range? (Y/N)\n")==True:
        xlim_l=IO.ReadFloat(qstStr="x-axis value (lowest): ")
        xlim_r=IO.ReadFloat(qstStr="x-axis value (highest): ")
        plt.xlim(xlim_l,xlim_r)

    if IO.YNDecision(decisionStr="Custom y-axis range? (Y/N)\n")==True:
        ylim_d=IO.ReadFloat(qstStr="y-axis value (lowest): ")
        ylim_u=IO.ReadFloat(qstStr="y-axis value (highest): ")
        plt.ylim(ylim_d,ylim_u)

    if IO.YNDecision(decisionStr="Custom x-axis label? (Y/N)\n")==True:
        xlabel=input("x-axis label: ")
        plt.xlabel(xlabel=xlabel)

    if IO.YNDecision(decisionStr="Custom y-axis label? (Y/N)\n")==True:
        ylabel=input("y-axis label: ")
        plt.ylabel(ylabel=ylabel)

    if IO.YNDecision(decisionStr="Custom title? (Y/N)\n")==True:
        title=input("Title: ")
        plt.title(label=title)

    if IO.YNDecision(decisionStr="Show line labels? (Y/N)\n")==True:

        valid:bool=False

        while valid==False:

            for i in range(len(legLoc)):
                print(f"Index: {i:^3} | Location: {legLoc[i]:^20}")

            legLocIndex=IO.ReadInt(qstStr="Location index: ")

            if legLocIndex not in range(len(legLoc)):
                print("Invalid input!")

            else:
                valid=True

        plt.legend(loc=legLoc[legLocIndex])

    if IO.YNDecision(decisionStr="Save graph as png? (Y/N)\n")==True:

        dirValid:bool=False
        nameValid:bool=False

        while dirValid==False:

            saveDir=input("Save at (dir): ")

            try:

                if os.path.isdir(saveDir)==False:
                    print(f"Directory ({saveDir:^50}) doesn't exists!")

                else:
                    dirValid=True

            except OSError:
                print("Invalid input!")

        while nameValid==False:

            saveName=input("Save as (name): ")
            absltName=saveDir+"/"+saveName+".png"

            try:
                if os.path.exists(absltName)==True:
                    print(f"File ({saveName:^20}.png) already exists!")

                    if IO.YNDecision("The file will be replaced if proceed, proceed? (Y/N)\n")==True:
                        nameValid=True

                else:
                    nameValid=True

            except OSError:
                print("Invalid input!")

        plt.savefig(absltName)

    input("Press any key to continue: ")
    plt.show()