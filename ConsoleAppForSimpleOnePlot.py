import SimpleOnePlot as simpPlt
import IOIwrote as IO

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

if __name__=="__main__":

    graph=simpPlt.Lines()

    xlim_l:float=None
    xlim_r:float=None
    ylim_d:float=None
    ylim_u:float=None
    xlabel:str=None
    ylabel:str=None
    title:str=None
    showLegend:bool=False
    legLocIndex:int=1
    legLoc:list=['best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center']

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

        if YNDecision(decisionStr="With label? (Y/N)\n")==True:
            label=input(f"Label for line {i:>3}: ")

        graph.AddLine(x=x,y=y,label=label)

        print("\n\n")

    if YNDecision(decisionStr="Custom x-axis range? (Y/N)\n")==True:
        xlim_l=IO.ReadFloat(qstStr="x-axis value (lowest): ")
        xlim_r=IO.ReadFloat(qstStr="x-axis value (highest): ")

    if YNDecision(decisionStr="Custom y-axis range? (Y/N)\n")==True:
        ylim_d=IO.ReadFloat(qstStr="y-axis value (lowest): ")
        ylim_u=IO.ReadFloat(qstStr="y-axis value (highest): ")

    if YNDecision(decisionStr="Custom x-axis label? (Y/N)\n")==True:
        xlabel=input("x-axis label: ")

    if YNDecision(decisionStr="Custom y-axis label? (Y/N)\n")==True:
        ylabel=input("y-axis label: ")

    if YNDecision(decisionStr="Custom title? (Y/N)\n")==True:
        title=input("Title: ")

    showLegend=YNDecision(decisionStr="Show line labels? (Y/N)\n")
    if showLegend==True:

        valid:bool=False

        while valid==False:

            for i in range(len(legLoc)):
                print(f"Index: {i:^3} | Location: {legLoc[i]:^20}")

            legLocIndex=IO.ReadInt(qstStr="Location index: ")

            if legLocIndex not in range(len(legLoc)):
                print("Invalid input!")

            else:
                valid=True

    input("Press any key to continue: ")
    simpPlt.CreateGraph(lns=graph.lns,xlim_l=xlim_l,xlim_r=xlim_r,ylim_d=ylim_d,ylim_u=ylim_u,xlabel=xlabel,ylabel=ylabel,title=title,withLegend=showLegend,legendLoc=legLoc[legLocIndex])