from audioop import rms
import math
import time
#from  matplotlib import pyplot as pp
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
        self.inlinks=[] 

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
        #self.shape=None

#    def setShape(self,shape):
#        self.shape=shape

    def setOutnodes(self,nodes):
        self.outnodes = tuple(nodes)

    def calculateMatrix(self,):
        vectorout=[]
        for node in self.outnodes:
            valout = node.calculateOutValue()
            vectorout.append(valout)
        return vectorout

    def printTset(self):
        tset=[]
        for node in self.outnodes:
            row=[]
            for ii in range(len(node.inlinks)):
                val = node.inlinks[ii].innode.val
                row.append(val)
            tset.append(row)
        print(tset)

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
    #print(neur.outnodes[0].inlinks[5].weight)
    #print(neur.outnodes[1].inlinks[5].weight)
    mat = neur.calculateMatrix()
    exponentials=[]
    for i in mat:
        exponentials.append(math.exp(i))
    sumexpo = sum(exponentials)
    softmaxval = []
    for val in exponentials:
        softmaxval.append(val/sumexpo)
    #a=math.exp(mat[0])/(math.exp(mat[0])+math.exp(mat[1]));#print(a)
    #b=math.exp(mat[1])/(math.exp(mat[0])+math.exp(mat[1]));#print(b)
    #softmaxval = [a,b]#.append([a,b])
    #assert abs(1-(a+b))<1*10**-5, 'a+b moet 1 zijn, dat is hier niet het geval'

    return softmaxval

def rootmeansquare (softmaxlist,trainingsets):
    """
    Omwerken van de softmax-waarschijnlijkheden van de  verschillende trainingsets naar een Root Mean Square. 
    sofmax-
    input:
        softmaxlist: lijst resultaten van verschillende softmaxscores  []
        trainingsets:  trainings invoer voor het neurale netwerk.
   
    NB1 De methode gaat uit van 2 outputnodes!
    NB2 De softmaxlist en de trainingset corresponderen met elkaar. 
    """

    def loss_function(probs,label):
        loss=0
        for i in range(len(probs)):
            error= label[i]-probs[i]
            sqerror=  error**2
            loss+=sqerror
        return loss

    loss=0
    for i in range(len(softmaxlist)):
        labels = scoretabel[trainingsets[i][3]]
        probabilities = softmaxlist[i]
        loss += loss_function(probabilities,labels)
    
        #a = softmaxlist[i][0]-scoretabel[trainingsets[i][3]][0] # op O waarde 
        #b = softmaxlist[i][1]-scoretabel[trainingsets[i][3]][1] # op O waarde 
    """
    for i in range(len(softmaxlist)):
        a = softmaxlist[i][0]-scoretabel[trainingsets[i][3]][0] # op O waarde 
        b = softmaxlist[i][1]-scoretabel[trainingsets[i][3]][1] # op O waarde 
        #print(a)
        #print(b)
        loss += a**2+b**2
    """

    rms = math.sqrt((loss/len(softmaxlist)))
        #rms+=b # op X-waarde 
    return rms

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
    
    #neural.outnodes[0].inlinks[0].setWeight(10)
    #Eerste berekening, met wf =1
    neural = initNetwork()
    tnow= time.time()


    softmaxl=[]
    for trainingset in trainingsets:
        i=0
        for tset in trainingset[:-1]: 
            for val in tset:
                neural.outnodes[0].inlinks[i].innode.setInvalue(val)
                neural.outnodes[1].inlinks[i].innode.setInvalue(val)
                i+=1
    softmaxval=softmax(neural)
    softmaxl.append(softmaxval)
    rms_0 = rootmeansquare(softmaxl,trainingsets)
    
    wfstep =0.0001
    #wf2rms=[]    #wflist=[] #costlist=[]
    
    while time.time()-tnow<4:
            #optimaliser = True
        for onnr in [0,1]: #iterate output nodes 
            for lnr in range(0,9): #iterate links bij outputnodes  
                wf = neural.outnodes[onnr].inlinks[lnr].weight#wf=100 # nog netter maken!
                print('link',str(lnr))
                print(neural.outnodes[onnr].inlinks[lnr].weight)
                loopdir = '+'
                #lnr = 5
                rms_p = rms_0
                for tel in range(3):
                    if loopdir=='+':
                        wf = wf+wfstep
                    else:# loopdir=='-':
                        wf = wf-wfstep
                    softmaxl=[]
                    neural.outnodes[onnr].inlinks[lnr].setWeight(wf)
                    for trainingset in trainingsets:
                        i=0
                        for tset in trainingset[:-1]: 
                            for val in tset:
                                neural.outnodes[0].inlinks[i].innode.setInvalue(val)
                                neural.outnodes[1].inlinks[i].innode.setInvalue(val)
                                i+=1
                        softmaxval=softmax(neural)
                        softmaxl.append(softmaxval)

                    rms = rootmeansquare(softmaxl,trainingsets)
                    if rms>rms_p:
                        if loopdir == '+':
                            loopdir = '-'
                        else:
                            optimaliser=False # optimalisatie wf afgelopen. Ga door naar volgende link
                            print('link',str(lnr))
                            print('\t wf = ',str(wf) )
                            neural.outnodes[onnr].inlinks[lnr].setWeight(wf)
                    rms_p= rms


                #print('c:',str(rms))
                
                
                #wflist.append(wf/100)
                #rmslist.append(rms)


