import unittest
from numpy_matrix import Matrix
import numpy as np
#from class_matrix import Matrix as Clmatrix



class matrixTest(unittest.TestCase):
    A = ((2,2,2),
        (3,3,3),
        (4,4,4),
        (5,5,5),)

    B = ((2,1),
        (2,3),
        (2,3))

    C = ((2,2,2),
        (3,3,3),
        (4,4,4),
        (5,5,5),)

    #Clmatri
    matA= Matrix(3,3)
    matB= Matrix(3,3)
    matC= Matrix(3,3)
    matA.set_matrix(A)
    matB.set_matrix(B)
    matC.set_matrix(C)
    #matA.multiply_matrix(matB)

    def test_multiplication(self):
        controledata = [[12, 14], [18, 21], [24, 28], [30, 35]]
        print(type(controledata))
        print(self.matA)
        print(self.matB)
        print(self.matA.multiply_matrix(self.matB))
        self.assertEqual(self.matA.multiply_matrix(self.matB).tolist(),
            controledata)
    
    def test_addition(self):
        controledata = [[ 4,  4,  4], [ 6,  6,  6], [ 8,  8,  8], [10, 10, 10]]
        self.assertEqual(self.matA.add_matrix(self.matC).tolist(),controledata)

if __name__=='__main__':
    unittest.main()
