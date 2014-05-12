'''
Created on May 11, 2014

@author: sameer
'''
import unittest
from HelloWorld.HelloWorld import hello_world

class Test(unittest.TestCase):

    def testPrintHelloWorld(self):
        self.assertEquals(hello_world(),"Hello, world!","Hello World function failed")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()