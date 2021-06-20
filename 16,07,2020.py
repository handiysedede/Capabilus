from sklearn import preprocessing
import numpy as np

a = np.random.random((1,4))
a = a*200
print("Datamız=  ",a)

normalized = preprocessing.normalize(a)
print("Abicim bana gelişi= ", normalized)

#%%
gat=["abo","cabo","zay"]
gat.sort()
print(gat)
gat.reverse()
print(gat)