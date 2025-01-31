import math
import pprint
trainingsets = (
    ((1,1,1),
    (1,0,1),
    (1,1,1),
    'O'),

    ((0,1,0),
    (1,0,1),
    (0,1,0),
    'O'),

    ((0,1,0),
    (1,1,1),
    (0,1,0),
    'X'),

    ((1,0,1),
    (0,1,0),
    (1,0,1),
    'X'),
    )

scoretabel = {'O':[0,1],'X':[1,0]} # scoretabel 
class Node:
    def __init__(self,):
        self.val=None
        self.inlinks=[] #len(x)*len Y
    def setInvalue(self,value):
        self.val = value
    def setInlinks(self, inlinks):
        for li in inlinks:
            self.inlinks.append(li)
    def calculateOutValue(self,):
        valout=0
        for li in self.inlinks:
            weight = li.weight
            valin =li.innode.val
            #for weight in li.innodes:
            valout += valin*weight
        return valout
class Link:
    def __init__(self,):
        self.weight=None
        self.innode = None
    def setInnode(self,node):
        self.innode = node
    def setWeight(self,weight):
        self.weight=weight

class Neural():
    def __init__(self):
        self.outnodes = []
        self.weightmat_old = {}
        self.weightmat_new = {}
        self.scoretabel = {'O':[0,1],'X':[1,0]} 
        self.shape=None
        
        #self.scorerms_old=[None,None]
        #self.scorerms_new=[None,None]
        #self.trainingsets = []

    def setShape(self,shape):
        self.shape=shape
    #def setTrainingsets(self,trainingsets):
    #    self.trainingsets = trainingsets

    def setOutnodes(self,nodes):
        self.outnodes = tuple(nodes)

    # def setWeightmatrix(self,weightmatrix):
    #     self.weightmat_old = self.weightmat_new
    #     self.weightmat_new = weightmatrix
    #     #weightmatrix_new
        
    #     for  node in self.outnodes:
    #         for inlink in node.inlinks:
    #             inlink

    def calculateMatrix(self,):
        vectorout=[]
        for node in self.outnodes:
            valout = node.calculateOutValue()
            vectorout.append(valout)
        return vectorout
            #for link in node.inlinks:
            #    link 


def softmax(neur):
    """
    genormaliseerde testscore van een matrix berekening op basis van resultaten neuraal netwerk
    Uitgangspunt is aanwezigheid 2 output nodes.
    normalisatie gebeurd met de softmaxvergelijking.  
    input: 
        neur, [Neural-object]
    output: 
        softmaxval, [[a,b]: a = softmaxwaarde node 1; b= softmaxwaarde node 2,   ]  
    """
       
    mat = neur.calculateMatrix()
    a=math.exp(mat[0])/(math.exp(mat[0])+math.exp(mat[1]))
    b=math.exp(mat[1])/(math.exp(mat[0])+math.exp(mat[1]))
    #print(a)
    #print(b)
    softmaxval = [a,b]#.append([a,b])

    return softmaxval

def costfunction(softmaxlist,trainingsets):
    """
    Omwerken van de softmax-scores verschillende trainingsets naar een totaalscore. 
    sofmax-
    input:
        softmaxlist: lijst resultaten van verschillende softmaxscores  []
        trainingsets:  trainings invoer voor het neurale netwerk.
   
    NB1 De methode gaat uit van 2 outputnodes!
    NB2 De softmaxlist en de trainingset corresponderen met elkaar. 
    """
    cost=0
    for i in range(len(softmaxlist)):
        a = softmaxlist[i][0]-scoretabel[trainingsets[i][3]][0] # op O waarde 
        #b = softmaxlist[i][1]-scoretabel[trainingsets[i][3]][1] # op O waarde 
        #print(a)
        #print(b)
        cost += a**2#+b**2
    cost = math.sqrt((cost/len(softmaxlist)))
        #cost+=b # op X-waarde 
    return cost

def initNetwork():
    #initialiseren van het netwerk. 
    neural= Neural()
    outnodeX= Node()
    outnodeO= Node()
    neural.setOutnodes([outnodeX,outnodeO])
    for tset in trainingsets[0][:-1]: 
        for val in tset:
            inlinka = Link()
            inlinkb = Link()
            # for val in row:
            innode = Node()
            innode.setInvalue(val)
            inlinka.setWeight(1)
            inlinka.setInnode(innode)
            inlinkb.setWeight(1)
            inlinkb.setInnode(innode)
            #if a>1:
            outnodeX.setInlinks([inlinka])
            #else:
            outnodeO.setInlinks([inlinkb])    
    return neural


if __name__=='__main__':
    
    neural = initNetwork()
    #neural.outnodes[0].inlinks[0].setWeight(10)
    #Eerste berekening, met wf =1

    wf2cost=[]

    for wf in range(10,1000,10):
        #Aanpassen van wf link 1 naar 10  
        neural.outnodes[1].inlinks[5].setWeight(wf/100)
        softmaxl=[]

        for trainingset in trainingsets:
            for tset in trainingset[:-1]: 
                i=0
                for val in tset:
                    neural.outnodes[0].inlinks[i].innode.setInvalue(val)
                    neural.outnodes[1].inlinks[i].innode.setInvalue(val)
                    i+=1
            softmaxval=softmax(neural)
            softmaxl.append(softmaxval)
        cost = costfunction(softmaxl,trainingsets)
        #print('c:',str(cost))
        wf2cost.append([wf/100,cost])
    pprint.pprint(wf2cost)


    """
    #initialiseren van het netwerk. 
    neural= Neural()
    outnodeX= Node()
    outnodeO= Node()
    neural.setOutnodes([outnodeX,outnodeO])
    for tset in trainingsets[0][:-1]: 
        for val in tset:
            inlinka = Link()
            inlinkb = Link()
            # for val in row:
            innode = Node()
            innode.setInvalue(val)
            inlinka.setWeight(1)
            inlinka.setInnode(innode)
            inlinkb.setWeight(1)
            inlinkb.setInnode(innode)
            #if a>1:
            outnodeX.setInlinks([inlinka])
            #else:
            outnodeO.setInlinks([inlinkb])
    """

    """
    softmaxl=[]
    for trainingset in trainingsets:
        for tset in trainingset[:-1]: 
            i=0
            for val in tset:
                neural.outnodes[0].inlinks[i].innode.setInvalue(val)
                neural.outnodes[1].inlinks[i].innode.setInvalue(val)
                i+=1
        softmaxval=softmax(neural)
        softmaxl.append(softmaxval)
    out = costfunction(softmaxl,trainingsets)
    print('c:',str(out))
    """

    #softmaxl=[]
    #for trainingset in trainingsets:
        #neural= Neural()
        #outnodeX= Node()
        #outnodeO= Node()
        #neural.setOutnodes([outnodeX,outnodeO])
    #    i=0

    #for trainingset in trainingsets:
    #    for tset in trainingset[:-1]: 
    #        for val in tset:
                #inlinka = Link()
                #inlinkb = Link()
                # for val in row:
                #innode = Node()
                #innode.setInvalue(val)
                #inlinka.setWeight(1)
                #inlinka.setInnode(innode)
                #inlinkb.setWeight(1)
                #inlinkb.setInnode(innode)
                #if a>1:
                #outnodeX.setInlinks([inlinka])
                #else:
                #outnodeO.setInlinks([inlinkb])
                #print(softmaxval)

        #shape = trainingset[0][-1]        
        #neural.setShape(shape)
        #neurals.append(neural)
        #neural.outnode.setInlink(Link())

    #neurals[0].outnodes[0].inlinks[0].setWeight(0.1)
    
    #softmaxl=softmax(neurals)
    #print(softmaxl)
    #print(outnodeX)
    #out = costfunction(softmaxl,trainingsets)
    #print('c:',str(out))
   
    #neurals[0].outnodes[0].inlinks[0].setWeight(10)
    
    
    # softmaxl=softmax(neurals)
    # out = costfunction(softmaxl,trainingsets)
    # print('c:',str(out))

    # neurals[0].outnodes[0].inlinks[0].setWeight(3)
    # softmaxl=softmax(neurals)
    # out = costfunction(softmaxl,trainingsets)
    # print('c:',str(out))
    
    
    #neural = Neural()
    #print(len(neural.outnodes[0].inlinks))
    #print(neural.calculateMatrix())
    #neural.setWeightmatrix(startweightmatrix)

    #neural.inlinks.

                    #print(tset[1])
                
 


"""

    linklist=[] 
    
    for weight in startweightmatrix:
        li = Link()
        li.setWeight(weight)
        li.setInnode()
        linklist.append(li)
    
    #output = dict({'X':[],'O':[]})
    for tset in trainingset[0:1]:
        outputO=Node()
        outputX=Node()
        for nrow in tset:
            print(nrow)
            for val in nrow:
                n=Node()
                n.setInValue(val)
                li =Link(weigth) 
                li.setInnode(n)
                print(li)
                xx
#trainingset2 = (1,1,1,1,0,1,1,1,1)

trainingset =(
    ((1,1,1),
    (1,0,1),
    (1,1,1),
    '0'),
(
(0,1,0),
(1,1,1),
(0,1,0)),
)

)
"""




