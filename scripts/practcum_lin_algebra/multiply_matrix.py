
import time
"""
- Maak list of lists A
- Maak list of lists B
    aanname: een list in list staat voor rij . 

-Controleer of afmetingen lists in A hetzelfde zijn 
-Controleer of afmetingen lists in B hetzelfde zijn 
-Controleer of lists A evenveel kolommen heeft als B rijen heeft 

Als één van bovenstaande voorwaarden niet geldt: stoppen!
4) Maak list C, met dimensie .... nog uitwerken!!!
Nu volgen de loops   
5) Start bij index [0,0] van A.
6a) Loop door rijindex B en en vermenigvuldig die met rij met zelfde index van A 
6b) Loop door rijindex A, aan einde ga naar 6c
6c) Loop door kolom B
7) Zet resultaat in  C[0,0]........Lopen moet verder uitgewerkt worden. 





"""

def multiply_vector(A,B):
    f =[len(a) for a in A ]
    g =[len(a) for a in B ]
    print(f)
    print(g)
    if len(set(f))!=1:
        print(f)
        raise Exception('verschillende afmetingen voor A en B')
    if len(set(g))!=1:
        raise Exception('verschillende afmetingen voor A en B')
    if len(A[0])!=len(B):
        raise Exception('A heeft niet zelfde aantal kolommen als B aan rijen heeft')
    
    C=[]
    for t in range(len(A)):
        C.append([0 for y in range(len(B[0]))])

    for ii in range(len(B[0])):
        Ccol=[]
        for r in range(len(A)):
            c=0
            for i in range(len(B)):
                #print(B[i][ii])
                c=c+A[r][i]*B[i][ii]
            C[r][ii]=c
            #Ccol.append(c)
            print(r,ii)    
            print(c)
            time.sleep(1)
        #C.append(Ccol)
        #while tel<len(A):
        #print(c)
        #C[i][ii]=c
        #C.append(Ccol)
        #print(C)
    return C
A= ((2,2,2),
    (3,3,3),
    (4,4,4),
    (5,5,5),
    )
B=((2,1),
   (2,3),
   (2,3))
b= multiply_vector(A,B)
print(b)

[[12, 14], 
 [18, 21], 
 [24, 28], 
 [30, 35]]
