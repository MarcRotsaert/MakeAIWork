import math

test = {'O':[0,1],'X':[1,0]} # scoretabel 
class Node:
    def __init__(self,):
        self.val=None
        self.inlinks=[] #len(x)*len Y
    def setInValue(self,value):
        self.val = value
    def setInlinks(self, inlinks):
        for li in inlinks:
            self.append(li)
    def calculateOutValue(self,):
        valout=[]
        for li in self.inlinks:
            for weight in li.nodes:
                self.val= self.val+self.val*weight
        return val
class Link:
    def __init__(self,weight):
        self.weight=weight
        self.node = None
    def setInNode(self,node):
        self.node = node

def softmax(outnodes):
    #total =0
    temp=[]
    for node in outnodes:
        temp.append(math.exp(node.calculateOutput()))
    print(temp[0]/sum[temp])
    print(temp[1]/sum[temp])

def costfunction(temp):
    for rms in softmaxlist:
        rms-

if __name__=='__main__':
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

    output = dict{'X':[],'O':[]}
    for tset in trainingset[0:1]:
        outputO=Node()
        outputX=Node()
        for nrow in tset:
            print(nrow)
            for node in nrow:
                outnode
                n=Node(n)
                li =Link(n) 

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




