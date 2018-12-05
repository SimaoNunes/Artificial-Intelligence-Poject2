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

        total          = 0
        size           = len(evid)
        targetID       = None
        subTargetsID   = []
        hiddenValuesID = [] 

        for i in range(0, size):
            e = evid[i]
            if e == -1:
                targetID = i
            elif e == 1:
                subTargetsID.append(i)
            elif e == []:
                hiddenValuesID.append(i)

        #alpha
        ev = ajudante(size, subTargetsID)
        total += 1 / self.computeProb(ev)[1]

        #target
        ev = ajudante(size, [targetID])
        total += self.computeProb(ev)[1]

        #hidden values
        for i in hiddenValuesID:

        return 0



        
    def computeJointProb(self, evid):
        total = 1
        for i in range(0,len(evid)):
            total *= self.prob[i].computeProb(evid)[evid[i]]
        return total


def ajudante(size,ids):
    ev = [0] * size
    for id in ids:
        ev[id] = 1
    return ev


    


# gra = [[],[],[0,1],[2],[2]]
# p1 = Node( np.array([.001]), gra[0] ) # burglary
# p2 = Node( np.array([.002]), gra[1] ) # earthquake
# p3 = Node( np.array([[.001,.29],[.94,.95]]), gra[2] ) # alarm
# p4 = Node( np.array([.05,.9]), gra[3] ) # johncalls
# p5 = Node( np.array([.01,.7]), gra[4] ) # marycalls
# prob = [p1,p2,p3,p4,p5]
# gra = [[],[],[0,1],[2],[2]]
# bn = BN(gra, prob)

# ev = (1,1,1,1,1)
# jp = []
# for e1 in [0,1]:
#     for e2 in [0,1]:
#         for e3 in [0,1]:
#             for e4 in [0,1]:
#                 for e5 in [0,1]:
#                     jp.append(bn.computeJointProb((e1, e2, e3, e4, e5)))
# print(jp)
# print("sum joint %.3f (1)" % sum(jp))
