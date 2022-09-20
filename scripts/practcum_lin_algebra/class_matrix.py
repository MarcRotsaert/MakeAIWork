
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
    matA = Matrix(rowlena,collena)
    matA.set_random_matrix()
    print('afmetingen matrix A:')
    matA.print_matsize()
    time.sleep(5)  
    matB = Matrix(collena,collenb)
    matB.set_random_matrix()
    print('afmetingen matrix B:')
    #self.print_matsize()
    time.sleep(5)  
    matresult = matA.multiply_matrix(matB)
    return matresult 


class Matrix:
    def __init__(self,rowlen,kollen):
        self.matrix=self._make_zero_matrix(rowlen,kollen)
        #self.matB=self._make_zero_matrix(kollen,rowlen)

    def _make_zero_matrix(self,rowlen=3,kollen=3):
        C=[]
        for t in range(rowlen):
            C.append([0 for y in range(kollen)])
        return C

    

    def set_random_matrix(self,):
        """
        Maak 2D matrix met afmeting rowsize bij kolsize.  
        """
        #randommat = make_zero_matrix(self,rowsize,kolsize)
        kolsize=len(self.matrix[0])
        rowsize=len(self.matrix)
        for k in range(kolsize):
            for r in range(rowsize):
                self.matrix[r][k]= random.randint(-100,100)
        #return randommat

    def calculate_average_matrix(self,):
        """
        Bereken gemiddelde van een matrix
        """
        total=0
        for row in self.matrix:
            for val in row:
                total=+val
        average  = total/(len(row)*len(self.matrix))
        return average

    def add_matrix(self, matB ):
        addmat = self._make_zero_matrix(len(matB.matrix),len(matB.matrix[0]))
        for i in range(len(matB.matrix)):
            for j in range(len(matB.matrix[i])):
                addmat[i][j] =self.matrix[i][j]+matB.matrix[i][j]
        return addmat

            

    def multiply_matrix(self,matB):
        """
        Vermenigvuldig  2D matrix A met 2D matrix B.

        """
        f = [len(a) for a in self.matrix ]
        g = [len(a) for a in matB.matrix ]
        #print(f)
        #print(g)
        if len(set(f))!=1:
            print(f)
            raise Exception('verschillende afmetingen voor A en B')
        if len(set(g))!=1:
            raise Exception('verschillende afmetingen voor A en B')
        if len(self.matrix[0])!=len(matB.matrix):
            raise Exception('A heeft niet zelfde aantal kolommen als B aan rijen heeft')
        
        C = self._make_zero_matrix(len(self.matrix),len(matB.matrix[0]))    
        C = []
            
        for t in range(len(self.matrix)):
            C.append([0 for y in range(len(matB.matrix[0]))])

        for ii in range(len(matB.matrix[0])):
            Ccol=[]
            for r in range(len(self.matrix)):
                c=0
                for i in range(len(matB.matrix)):
                    #print(matB[i][ii])
                    c=c+self.matrix[r][i]*matB.matrix[i][ii]
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



    def print_matsize(self,):
        """
        print  afmetingen van de matrix.
        """
        print("aantal rijen = "+str(len(self.matrix)))
        print("aantal kolommen = "+str(len(self.matrix[0])))

if __name__=='__main__':

    import pprint

    if False:
        result = make_random_matrixmultiplication()
        resultcopy = result.copy()
        result
        print(result)
    if False:
        #F = make_zero_matrix(5,3)
        matresult = make_random_matrixmultiplication()
        average = self.calculate_average_matrix()
        
        pprint.pprint(matresult)
        print(average)
        print_matsize(matresult)

    if True:
            A = Matrix(50,40)
            A.set_random_matrix()
            B = Matrix(50,40)
            B.set_random_matrix()
            A.add_matrix(B)
            b= A.add_matrix(B)

            print(b[20][20])
            print(A.matrix[20][20])
            print(B.matrix[20][20])
            #average = calculate_average_matrix(b)
            #pprint.pprint(b)
            #print(average)
            print_matsize(b)



    if False:
        A = set_random_matrix(50,30)
        B = set_random_matrix(30,20)
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