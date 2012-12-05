#coding: utf-8

import os, sys

class TestClass:
    """This is a test class
    """
    def __init__(self, name):
        self.name = name
        
    def printme(self):
        print self.name
        
if __name__ == "__main__":
    a = TestClass("hello")
    a.printme()