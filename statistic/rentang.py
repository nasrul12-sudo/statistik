class rentang:
    def __init__(self, min, max, vall):
        self.min = min
        self.max = max
        self.vall = vall
        
    def rangeVall(self):
        return self.max-self.min
        
    def Mclass(self):
        vall = self.vall
        log_2 = 0.301
        log_3 = 0.477
        log_5 = 0.699
        log_7 = 0.845

        log = len(vall)/10
        if log/2 == 1:
            log1 = 3.3 * (log_2 + 1)
            return (log1 + 1)

        if log/3 == 1:
            log1 = 3.3 * (log_3 + 1)
            return (log1 + 1)
        
        if log/5 == 1:
            log1 = 3.3 * (log_5 + 1)
            return (log1 + 1)
        
        if log/7 == 1:
            log1 = 3.3 * (log_7 + 1)
            return (log1 + 1)
        
def Lclass(Mclass, min, max):
    return ((max-min)/Mclass)
            