"""
- Maak list of lists A
- Maak list of lists B
    aanname: komma scheiding staat voor een nieuwe kolom. 

-Controleer of afmetingen lists in A hetzelfde zijn 
-Controleer of afmetingen lists in B hetzelfde zijn 
-Controleer of lists A evenveel rijen heeft als B kolommen heeft 

Als één van bovenstaande manieren niet: stoppen!
4) Maak list C   
5) Ga iedere index van cel af en vermenigvuldig die met cel met zelfde index van B
6) tel resultaten uit voorafgaande test op.
"""

def multiply_vector(A,B):
    f =[len(a) for a in A ]
    g =[len(a) for a in B ]
    if len(set(f))!=1:
        print(f)
        raise Exception('verschillende afmetingen voor A en B')
    if len(set(g))!=1:
        raise Exception('verschillende afmetingen voor A en B')
    if len(A)!=len(B[0]):
        raise Exception('A heeft niet zelfde aantal rijen als B aan kolommen heeft')
    C=[]
    for i in range(len(A)):
        c=0
        for ii in range(len(B[0])):
            print(type(i))
            print(type(ii))
            A[i,ii]
            B[i,ii]

            c=c+A[i,ii]*B[ii,i]
            #while tel<len(A):
        C[i,ii]=c
    #C=(C)
    #print(C)
    return C
A= ((2,2,2),(2,3,3));B=((2,2),(2,3),(2,3))
b= multiply_vector(A,B)
print(b)


