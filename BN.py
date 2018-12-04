# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np

class Node():
    def __init__(self, prob, parents = []):
        self.prob    = prob
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
        self.graph = gra
        self.prob  = prob

    def computePostProb(self, evid):
        return 0
        
    def computeJointProb(self, evid):
        total = 0
        for i in range(0,len(self.prob)):
            total += self.prob[i].computeProb(evid)[evid[i]]               
        return total