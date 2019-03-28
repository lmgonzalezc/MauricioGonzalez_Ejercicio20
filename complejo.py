import numpy as np
import unittest
import math
class Complejo():
    def __init__ (self, Imag, Real):
        self.imaginario=Imag
        self.real=Real
        self.norma=np.sqrt(Imag**2+Real**2)
    def conjugado(self):
        self.imaginario=-self.imaginario
    def calcula_norma(self):
        self.norma=np.sqrt(Imag**2+Real**2))
    def pow(self, power):
        return ((self.real+self.imaginario)**power)
        
