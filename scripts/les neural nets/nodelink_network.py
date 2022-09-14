import math

inputsets = (
    ((1,1,1),
    (1,0,1),
    (1,1,1),
    '0'),

    ((0,1,0),
    (1,0,1),
    (0,1,0),
    '0'),

    ((0,1,0),
    (1,1,1),
    (0,1,0),
    'X'),

    ((1,0,1),
    (0,1,0),
    (1,0,1),
    'X'),
    )

#scoretabel = {'O':[0,1],'X':[1,0]} # scoretabel 
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


def softmax(trainingsets):
    #for tset in trainingsets:

        #total =0
        #temp=[]
        #for node in outnodes:
        temp.append(math.exp(neural.calculateOutput()))
        #print(temp[0]/sum(temp))
        #print(temp[1]/sum(temp))
    return softmaxlist

def costfunction(softmaxlist):
    for rms in softmaxlist:
        rms

if __name__=='__main__':
    
    #def calculateoutnode   
    print(trainingset)
    #startweightmatrix = 18*[1]
    
    for trainingset in inputsets:
        neural= Neural()
        outnodeX= Node()
        outnodeO= Node()
        neural.setOutnodes([outnodeX,outnodeO])
        for tset in trainingset[1][:-1]: 
            for val in tset:
                # for val in row:
                innode = Node()
                innode.setInvalue(val)
                inlinka = Link()
                inlinkb = Link()
                inlinka.setWeight(1)
                inlinka.setInnode(innode)
                inlinkb.setWeight(1)
                inlinkb.setInnode(innode)
                #if a>1:
                outnodeX.setInlinks([inlinka])
                #else:
                outnodeO.setInlinks([inlinkb])

        shape = trainingset[0][-1]        
        neural.setShape(shape)
        #neural.outnode.setInlink(Link())

        #innode=Node()
        #innode.setInValue()
        #    inlink = Link()
    print(outnodeO)
    print(outnodeX)

    #neural = Neural()
    print(len(neural.outnodes[0].inlinks))
    print(neural.calculateMatrix())
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




