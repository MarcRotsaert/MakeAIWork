import os
#from class_matrix import Matrix
import numpy as np
import pprint
import random

if False:
    A = Matrix(50,40)
    A.set_random_matrix()
    B = Matrix(50,40)
    B.set_random_matrix()
    result= A.add_matrix(B)
    pprint.pprint(result)
    A_np = np.array(A.matrix)
    B_np = np.array(B.matrix)
    result_np = A_np+B_np
    pprint.pprint(result_np)

class Matrix:
    def __init__(self,rowlen,kollen):
        self.matrix = self._make_zero_matrix(rowlen,kollen)

    def _make_zero_matrix(self,rowlen=3,kollen=3):
        return np.zeros([rowlen,kollen])

    def set_random_matrix(self,):
        self.matrix=np.random.rand(self.matrix.shape[0],self.matrix.shape[1])

    def set_matrix(self,vectorlist):
        self.matrix = np.array(vectorlist)

    def add_matrix(self, matB ):
        return self.matrix+matB.matrix

    def multiply_matrix(self, matB ):
        return np.dot(self.matrix,matB.matrix)

if False:
    A = Matrix(10,20)
    A.set_random_matrix()
    B = Matrix(30,10)
    B.set_random_matrix()
    resultm = B.multiply_matrix(A)
    np.array(resultm)
    pprint.pprint(resultm)

    A_np = np.array(A.matrix)
    B_np = np.array(B.matrix)
    resultm_np = np.dot(B_np,A_np)
    resultm_np2 = np.dot(B.matrix,A.matrix)
    pprint.pprint(resultm_np)
    pprint.pprint(resultm_np2)
    print(np.array_equal(resultm_np,resultm_np2))
    print(np.array_equal(resultm_np,np.array(resultm)))

    np.savez('c:/temp/resultarray.npz',resultm_np)
    np.save('c:/temp/resultarray',resultm_np)
if True:
    A = ((2,2,2),
        (3,3,3),
        (4,4,4),
        (5,5,5),
        )
    B = ((2,1),
    (2,3),
    (2,3))


    matA= Matrix(3,3)
    matB= Matrix(3,3)
    matA.set_matrix(A)
    matB.set_matrix(B)
    print((matA.multiply_matrix(matB)))

    C = ((2,2,2),
        (3,3,3),
        (4,4,4),
        (5,5,5),
        )

    matC = Matrix(4,3) 
    matC.set_matrix(C)
    print((matA.add_matrix(matC)))
