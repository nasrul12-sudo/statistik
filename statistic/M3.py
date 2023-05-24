class M3:
    def __init__(self, arr):
        self.arr = arr
        
    def mean(self):
        jlm = 0
        for i in self.arr:
            jlm = jlm+i
            
        return (jlm/len(self.arr))
    
    def median(self):
        lenArr = len(self.arr)
        if(lenArr%2==0):
            me1 = lenArr/2
            me2 = (lenArr/2)+1
            return (me1+me2)/2
        
    def modulus(self):
        uniq_data = []; mode_value =    []
        
        for i in self.arr:
            if i not in uniq_data:
                uniq_data.append(i)
            else:
                mode_value.append(i)
        return mode_value
              