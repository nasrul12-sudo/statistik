import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Table:
    def __init__(self, Mclass, Lclass, arr, min, max):
        self.Mclass = Mclass
        self.Lclass = Lclass
        self.arr = arr
        self.min = min
        self.max = max
          
    def tables(self):
        #nilai interval
        nframe = []; Jml = []
        
        min = self.min
        min2 = self.min+1
        Jml.append(min)
        for i in range(self.Mclass):
            min+=self.Lclass
            nframe.append(min-1)
        
        for i in range(self.Mclass-1):
            min2+=self.Lclass
            Jml.append(min2)

        
        #frekuensi mutlak
        if(self.Mclass == 6):
            Dfrek = []; Lnfrek = []; nfrek1=[]; nfrek2=[]; nfrek3=[]; nfrek4=[]; nfrek5=[]; nfrek6=[]
            
            for i in self.arr:
                if(i<nframe[0]):
                    nfrek1.append(i)
                elif((i>nframe[0])&(i<nframe[1])):
                    nfrek2.append(i)
                elif((i>nframe[1])&(i<nframe[2])):
                    nfrek3.append(i)
                elif((i>nframe[2])&(i<nframe[3])):
                    nfrek4.append(i)
                elif((i>nframe[3])&(i<nframe[4])):
                    nfrek5.append(i)
                elif((i>nframe[4])&(i<nframe[5])):
                    nfrek6.append(i)
                    
            Lnfrek.append([nfrek1, nfrek2, nfrek3, nfrek4, nfrek5, nfrek6])
            for i in Lnfrek:
                for j in i:
                    Dfrek.append(len(j))
                    
        print("Nilai Interval")
        dframe = {
            'Batas Awal' : np.array(Jml), 
            'Batas Akhir' : np.array(nframe),
            'Frekuensi' : np.array(Dfrek)
        }
        dataframe = pd.DataFrame(dframe)
        print(dataframe)
        
        plt.figure(figsize=(8,4))
        plt.bar(dframe['Batas Akhir'],dframe['Frekuensi'])
        plt.xticks()
        plt.show()
                
        return Jml, nframe, Dfrek
                             
        
