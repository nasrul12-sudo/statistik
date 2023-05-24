import numpy as np

import frekuensiMutlak as fm
import rentang as r
import table as t
import M3 as M
import quartil as K
            

arr = np.array([23, 80, 52, 41, 60, 34, 60, 77, 10, 71, 79, 80, 64, 83, 89, 17, 32, 95, 75, 76, 70, 85,98, 62, 64, 55, 61, 56, 67, 61])
# arr = np.array([23, 85, 52, 41, 60, 34, 60, 87, 10, 79, 80, 80, 64, 80, 90, 19, 32, 95, 75, 76, 70, 85, 98, 62, 64, 55, 61, 56, 97, 61])
sort = fm.dfmutlak(arr)

min = sort.min(); print(f"min : {min}")
max = sort.max(); print(f"max : {max}")
rent = sort.sorted()

rentang = r.rentang(min, max, arr) 
rangeClass = rentang.rangeVall(); print(f"range class : {rangeClass}")
manyClass = rentang.Mclass(); rmanyClass = round(manyClass); print(f"many class : {round(rmanyClass)}")
lenClass = r.Lclass(manyClass, min, max); rlenClass = round(lenClass); print(f"len class : {rlenClass}")

M3 = M.M3(arr)
Mean = M3.mean(); print(f"Mean : {Mean}")
Median = M3.median();  print(f"Median : {Median}")
Modulus = M3.modulus(); print(f"Modulus : {Modulus}") 

kuartil = K.quartil(len(arr), arr)
Q = kuartil.Kuartil()
print(f"Q1 : {Q[0]}\nQ2 : {Q[1]}\nQ3 : {Q[2]}")

Table = t.Table(rmanyClass, rlenClass, arr, min, max)
Ttable = Table.tables()
