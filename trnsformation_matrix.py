class transformation_matrix():
    def __init__(self, datapoints):
        self.datapoints = datapoints
        self.x,self.y,self.m,self.n = np.zeros((self.datapoints)),np.zeros((self.datapoints)),np.zeros((self.datapoints)),np.zeros((self.datapoints))
                                                                            
        for i in range(self.datapoints):
            self.x[i] = input("Input x:")
            self.y[i] = input("Input y:")
            self.m[i] = input("Input m:")
            self.n[i] = input("Input n:")
    
    def compute_transformation_matrix(self):
        A = np.zeros((2*self.datapoints, 9))
        
        for j in range(self.datapoints):

            q = 2*j
            A[q,0] = self.x[j]
            A[q,1] = self.y[j]
            A[q,2] = 1
            A[q,3], A[q,4], A[q,5] = 0, 0, 0
            A[q,6] = -self.m[j]*self.x[j]
            A[q,7] = -self.m[j]*self.y[j]
            A[q,8] = -self.m[j]

            A[q+1,0], A[q+1,1], A[q+1,2] = 0, 0, 0
            A[q+1,3] = self.x[j]
            A[q+1,4] = self.y[j]
            A[q+1,5] = 1
            A[q+1,6] = -self.n[j]*self.x[j]
            A[q+1,7] = -self.n[j]*self.y[j]
            A[q+1,8] = -self.n[j]
            
        u, s, v = linalg.svd(A)
        v = v[-1,:]
        v = v.reshape(3,3)

        return v
