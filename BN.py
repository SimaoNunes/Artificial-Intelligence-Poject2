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
<<<<<<< HEAD
        self.gra = gra
        self.prob = prob
        pass
=======
        self.graph = gra
        self.prob  = prob
>>>>>>> f1660cba64b32b20c07b260782091e68a17e518a

    def computePostProb(self, evid):
        return 0
        
    def computeJointProb(self, evid):
        total = 1
        for i in range(0,len(evid)):
<<<<<<< HEAD
            total *= self.prob[i].computeProb(evid)[evid[i]]
        return total





gra = [[],[],[0,1],[2],[2]]
p1 = Node( np.array([.001]), gra[0] ) # burglary
p2 = Node( np.array([.002]), gra[1] ) # earthquake
p3 = Node( np.array([[.001,.29],[.94,.95]]), gra[2] ) # alarm
p4 = Node( np.array([.05,.9]), gra[3] ) # johncalls
p5 = Node( np.array([.01,.7]), gra[4] ) # marycalls
prob = [p1,p2,p3,p4,p5]
gra = [[],[],[0,1],[2],[2]]
bn = BN(gra, prob)






ev = (1,1,1,1,1)
jp = []
for e1 in [0,1]:
    for e2 in [0,1]:
        for e3 in [0,1]:
            for e4 in [0,1]:
                for e5 in [0,1]:
                    jp.append(bn.computeJointProb((e1, e2, e3, e4, e5)))
print(jp)
print("sum joint %.3f (1)" % sum(jp))
=======
            total = total *  self.prob[i].computeProb(evid)[evid[i]]               
        return total
>>>>>>> f1660cba64b32b20c07b260782091e68a17e518a
