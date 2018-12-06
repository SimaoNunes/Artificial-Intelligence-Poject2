# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np
import itertools

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
        self.gra = gra
        self.prob = prob


    def computePostProb(self, evid):
        unknownNodes = 0
        total = 0
        alpha = 0
        for e in evid:
            if e == []:
                unknownNodes += 1
        binary_list_true = list(itertools.product([0,1], repeat=unknownNodes))
        binary_list_alpha = list(itertools.product([0,1], repeat=unknownNodes+1))
        for i in range(0,2**unknownNodes):
            c = 0
            ev = ()
            for e in evid:
                if e == []:
                    ev = ev + (binary_list_true[i][c],)
                    c += 1
                else:
                    ev = ev + (abs(e),)
            total += self.computeJointProb(ev)
        for i in range(0,2**(unknownNodes+1)):
            c = 0
            ev = ()
            for e in evid:
                if e == [] or e == -1:
                    ev = ev + (binary_list_alpha[i][c],)
                    c += 1
                else:
                    ev = ev + (e,)
            alpha += self.computeJointProb(ev)
            
        return total/alpha

        
        
    def computeJointProb(self, evid):
        total = 1
        for i in range(0,len(evid)):
            total *= self.prob[i].computeProb(evid)[evid[i]]
        return total
