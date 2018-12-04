# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np

class Node():
    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents
    
    def computeProb(self, evid):
        if len(self.parents) == 0:
            return [ 1-self.prob[0], self.prob[0]]
        prob = self.prob
        for parent in self.parents:
            prob = prob[evid[parent]]
        return [1-prob, prob]

class BN():
    def __init__(self, gra, prob):
        pass

    def computePostProb(self, evid):
        pass
               
        return 0
        
        
    def computeJointProb(self, evid):
        pass
        
        return 0