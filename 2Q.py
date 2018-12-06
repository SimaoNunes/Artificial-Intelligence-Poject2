def traces2Q(self, trace):
                # implementar esta funcao
        self.Q = np.zeros((self.nS,self.nA))
        nQ = np.zeros((self.nS,self.nA))
        ii = 0
        while True:            
            for tt in trace:
                #[x, a, y, r]
                nQ[int(tt[0]),int(tt[1])] = nQ[int(tt[0]),int(tt[1])] + 0.01 * (tt[3] + self.gamma * max(nQ[int(tt[2]),:]) - nQ[int(tt[0]),int(tt[1])])
            ii = ii +1  
            err = np.linalg.norm(self.Q-nQ)
            self.Q = np.copy(nQ)
            if err<1e-2:
                break 

        return self.Q