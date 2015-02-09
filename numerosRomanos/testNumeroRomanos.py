'''
Created on 8/2/2015

@author: Jonnathan
'''
import unittest
from romanos import convertirRomano

class Test(unittest.TestCase):

    def testRomanoExiste(self):
        numero = convertirRomano('I')
    
    def testNumeroUno(self):
        numero = convertirRomano('I')
        self.assertEqual(numero, 1)
    
    def testNumeroCinco(self):
        numero = convertirRomano('V')
        self.assertEqual(numero, 5)
           
    def testNumeroDiez(self):
        numero = convertirRomano('X')
        self.assertEqual(numero, 10)
    
    def testNumeroUnico(self):
        self.assertEqual(convertirRomano('I'), 1)
        self.assertEqual(convertirRomano('V'), 5)
        self.assertEqual(convertirRomano('X'), 10)
        self.assertEqual(convertirRomano('L'), 50)
        self.assertEqual(convertirRomano('C'), 100)
        self.assertEqual(convertirRomano('D'), 500)
        self.assertEqual(convertirRomano('M'), 1000)
       
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()