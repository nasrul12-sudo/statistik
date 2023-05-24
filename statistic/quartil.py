class quartil:
    def __init__(self, Larr, arr):
        self.Larr = Larr
        self.arr = arr
        
    def Kuartil(self):
        if(self.Larr%2==0):
            q1 = 1/4*(self.Larr+1)
            Q1 = (self.arr[int(q1-1)] + self.arr[int(q1)])/2
            print("quartil1 : ", self.arr[int(q1)], self.arr[int(q1+1)])
            
            q2 = 1/2*(self.Larr+1)
            Q2 = (self.arr[int(q2-1)] + self.arr[int(q2)])/2
            
            q3 = 3/4*(self.Larr+1)
            Q3 = (self.arr[int(q3-1)] + self.arr[int(q3)])/2
            return Q1,Q2,Q3
            
                
        