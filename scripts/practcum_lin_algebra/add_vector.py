"""
1) Maak list A
2) Maak list B
3) Controleer of afmetingen A en B overeenkomen. 
    als afmeting A niet gelijk aan B
    als afmeting A gelijk aan B, ga naar volgende stap
4) Maak list C   
5) Ga iedere cel in list A  tel list A bij B op
"""

def add_vector(A,B):
    #if len(A)!=len(B):
        #raise 'verschillende afmetingen voor A en B'
    #    raise Exception('verschillende afmetingen voor A en B')
    tel=0
    C=[]
    while tel<len(A):
        C.append(A[tel]+B[tel])
        tel+=1
    C=(C)
    #print(C)
    return C
A= (1,2,3);B=(4,5,)
b= add_vector(A,B)
print(b)
