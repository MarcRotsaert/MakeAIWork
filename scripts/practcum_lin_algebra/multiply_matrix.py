
import time
"""
Vermenigvuldig 2D matrices met random afmetingen en random integers in range -100 tot 100 .


- Maak list of lists A met random
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
import random
def make_zero_matrix(rowlen=3,kollen=3):
    C=[]
    for t in range(rowlen):
        C.append([0 for y in range(kollen)])
    return C

def make_random_matrix(rowsize=3,kolsize=3):
    """
    Maak 2D matrix met afmeting rowsize bij kolsize.  
    """
    randommat = make_zero_matrix(rowsize,kolsize)
    for k in range(kolsize):
        for r in range(rowsize):
            randommat[r][k]= random.randint(-100,100)
    
    return randommat

def calculate_average_matrix(mat):
    """
    Bereken gemiddelde van een matrix
    """
    total=0
    for row in mat:
        for val in row:
            total=+val
    average  = total/(len(row)*len(mat))
    return average

def multiply_matrix(A,B):
    """
    Vermenigvuldig  2D matrix A met 2D matrix B.

    """
    f = [len(a) for a in A ]
    g = [len(a) for a in B ]
    #print(f)
    #print(g)
    if len(set(f))!=1:
        print(f)
        raise Exception('verschillende afmetingen voor A en B')
    if len(set(g))!=1:
        raise Exception('verschillende afmetingen voor A en B')
    if len(A[0])!=len(B):
        raise Exception('A heeft niet zelfde aantal kolommen als B aan rijen heeft')
    
    C = make_zero_matrix(len(A),len(B[0]))    
    C = []
        
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
            #print(r,ii)    
            #print(c)
            #time.sleep(1)
        #C.append(Ccol)
        #while tel<len(A):
        #print(c)
        #C[i][ii]=c
        #C.append(Ccol)
        #print(C)
    return C


def make_random_matrixmultiplication():
    """
    Maak een matrix berekening, met volgende eigenschappen 
    - 2 matrices worden met elkaar vermenigvuldigd. 
    - matrices hebben willekeurige afmeting tussen 2 en 100 rijen/kolommen
    - waarden in de matrices zijn willekeurige integers tussen -100 en 100,  
    """
    rowlena = random.randint(2,100)
    collena = random.randint(2,100)
    collenb = random.randint(2,100)
    A = make_random_matrix(rowlena,collena)
    print('afmetingen matrix A:')
    print_matsize(A)
    time.sleep(5)  
    B = make_random_matrix(collena,collenb)
    print('afmetingen matrix B:')
    print_matsize(B)
    time.sleep(5)  
    matresult = multiply_matrix(A,B)
    return matresult 

def print_matsize(mat):
    """
    print  afmetingen van de matrix.
    """
    print("aantal rijen = "+str(len(mat)))
    print("aantal kolommen = "+str(len(mat[0])))

if __name__=='__main__':
    import pprint
    #F = make_zero_matrix(5,3)
    matresult = make_random_matrixmultiplication()
    average = calculate_average_matrix(matresult)
    
    pprint.pprint(matresult)
    print(average)
    print_matsize(matresult)

    if False:
        A = make_random_matrix(50,30)
        B = make_random_matrix(30,20)
        b= multiply_matrix(A,B)
        average = calculate_average_matrix(b)
        pprint.pprint(b)
        print(average)
        print_matsize(b)
"""
    A = ((2,2,2),
        (3,3,3),
        (4,4,4),
        (5,5,5),
        )
    B = ((2,1),
    (2,3),
    (2,3))





    b= multiply_matrix(A,B)
    print(b)

    [[12, 14], 
    [18, 21], 
    [24, 28], 
    [30, 35]]
"""