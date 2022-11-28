from matplotlib import pyplot as plt

class Line:

    def __init__(self,x:list=[],y:list=[],label:str=None,color:str=None,marker:str=None,linestyle:str=None,linewidth:float=None,markersize:float=None):
        self.x:list=x
        self.y:list=y
        self.label:str=label
        self.color:str=color
        self.marker:str=marker
        self.linestyle:str=linestyle
        self.linewidth:float=linewidth
        self.markersize:float=markersize

class Lines:

    lns:list=[]

    def AddLine(self,x:list=[],y:list=[],label:str=None,color:str=None,marker:str=None,linestyle:str=None,linewidth:float=None,markersize:float=None):
        self.lns.append(Line(x=x,y=y,label=label,color=color,marker=marker,linestyle=linestyle,linewidth=linewidth,markersize=markersize))

def CreateGraph(lns:list=[],xlim_l:float=None,xlim_r:float=None,ylim_d:float=None,ylim_u:float=None,xlabel:str=None,ylabel:str=None,title:str=None,xticks_ticks:list=None,xticks_labels:list=None,yticks_ticks:list=None,yticks_labels:list=None,withLegend:bool=False,legendLoc:str=None):

    for i in range(len(lns)):
        plt.plot(lns[i].x,lns[i].y,label=lns[i].label,color=lns[i].color,marker=lns[i].marker,linestyle=lns[i].linestyle,linewidth=lns[i].linewidth,markersize=lns[i].markersize)

    plt.xlim(xlim_l,xlim_r)
    plt.ylim(ylim_d,ylim_u)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(ticks=xticks_ticks,labels=xticks_labels)
    plt.yticks(ticks=yticks_ticks,labels=yticks_labels)

    if withLegend==True:
        plt.legend(loc=legendLoc)

    plt.show()

if __name__=="__main__":

    graphSample=Lines()
    graphSample.AddLine(x=[1,2,3],y=[0,1,0],label="Line0",color="Red")
    graphSample.AddLine(x=[1,2,3],y=[0,1,0],label="Line1",color="Blue")

    CreateGraph(lns=graphSample.lns,xlim_l=0,xlim_r=5,ylim_d=-0.1,ylim_u=1.1,xlabel="x",ylabel="y",title="Graph0",withLegend=True,legendLoc="upper right")