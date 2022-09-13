import math

scoretabel = {'O':[0,1],'X':[1,0]} # scoretabel 
class Node:
    def __init__(self,):
        self.val=None
        self.inlinks=[] #len(x)*len Y
    def setInValue(self,value):
        self.val = value
    def setInlinks(self, inlinks):
        for li in inlinks:
            self.inlinks.append(li)
    def calculateOutValue(self,):
        valout=[]
        for li in self.inlinks:
            for weight in li.nodes:
                self.val= self.val+self.val*weight
        return val
class Link:
    def __init__(self,weight):
        self.weight=weight
        self.no_in = None
    def setInNode(self,node):
        self.no_in = node
    def setWeight(self,weight):
        self.weight=weight

def Neural(self,):
    self.outnodes = []
    #self.inlinks =[]
    self.weightmat_old = []
    self.weightmat_new = []
    self.scoretabel = {'O':[0,1],'X':[1,0]} 
    self.scorerms_old=[None,None]
    self.scorerms_new=[None,None]

    def setWeightmatrix(self,weightmatrix)
        self.weightmatrix_old(self.weightmat_new)
        self.weightmatrix_new(weightmatrix)
    def calculateMatrix(self,):
        for node in self.outnode:
            for link in node.inlinks:
                link 

    def setOutnodes(self,):

def softmax(outnodes):
    #total =0
    temp=[]
    for node in outnodes:
        temp.append(math.exp(node.calculateOutput()))
    print(temp[0]/sum(temp))
    print(temp[1]/sum(temp))

def costfunction(softmaxlist):
    for rms in softmaxlist:
        rms

if __name__=='__main__':
    startweightmatrix = 18*[1]
    weight
    for r in range(3):
        for c in range(3):
            ()



    trainingset = (
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




    linklist=[] 
    
    for weight in startweightmatrix:
        li = Link()
        li.setWeight(weight)
        li.setInNode()
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
                li.setInNode(n)
                print(li)
                xx
#trainingset2 = (1,1,1,1,0,1,1,1,1)

"""
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




