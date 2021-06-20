#r Read, a append, w write, x create
#print(f.read())
fileToAppend = open("dos.txt","w")
fileToAppend.write("\n")
fileToAppend.write("Ahmet")
fileToAppend.close()
#%% Dosyayı siler
import os
if os.path.exists("dos.txt"):
    os.remove("dos.txt")
else:
    print("Dosya yok")
#%% Klasörü siler
os.rmdir("rmdir")
#%%
'''
#Hepsini okur
print(f.read())
#satır datır okur ama birlikte kulllanılmaz
print(f.readlines(1))
#İterator yapar bütün lineları okur
for l in f:
    print(l)
#f.close()'''
