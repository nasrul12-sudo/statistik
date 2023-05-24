class dfmutlak:
    def __init__(self, vall):
        self.vall = vall
        
    def sorted(self):
        for i in range(len((self.vall)-1)):
            for j in range(len(self.vall)-i-1):
                if self.vall[j+1]<self.vall[j]:
                    self.vall[j], self.vall[j+1] = self.vall[j+1], self.vall[j]
        print(f"short : \n{self.vall}")
    
    def max(self):
        max = self.vall[0]
        for i in self.vall:
            if i > max:
                max = i
        return max
    
    def min(self):
        min = self.vall[0]
        for i in self.vall:
            if i < min:
                min = i
        return min
    