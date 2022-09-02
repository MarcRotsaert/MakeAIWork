"""
1) Maak list A
2) Maak list B
3) Controleer of afmetingen A en B overeenkomen. 
    als afmeting A niet gelijk aan B
    als afmeting A gelijk aan B, ga naar volgende stap
4) Maak list C   
5) Ga iedere index van cel af en vermenigvuldig die met cel met zelfde index van B
6) tel resultaten uit voorafgaande test op.
"""
def multiply_vector(A,B):
    if len(A)!=len(B):
        raise Exception('verschillende afmetingen voor A en B')
    tel=0
    C=0
    while tel<len(A):
        C=C+A[tel]*B[tel]
        tel+=1
    #C=(C)
    #print(C)
    return C
A= (2,2,2);B=(4,5,8)
bla= multiply_vector(A,B)
print(bla)


