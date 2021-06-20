

#%%Fİle yaşıyosa ekle
try:
    inputFile= open("InputFile.txt", "r")
except IOError as error:
        print("errorlendin")
else:
    for line in inputFile:
        print(line)
    inputFile.close()
i = open("InputFile.txt","a")  # \n yaparsan ve 'w' kullanırsan hepsini siler
i.write("The try block contains the code to attempt.• The except blocks contain the code to run if and only if an expected error type occurs.• The else block contains the code to run if and only if no errors occur.• The finally  block  contains  the  code  to  run  regardless  of  whether  or  not  an  error occurred.")
print(a)
#%%File yaşıyo mu ?
c=open("InputFile.txt","r")
print(c.readable())
#%%tam olarak şurayı atsana bana
print(c.readline()[0])
#%%Hepsini isterim
for i in c.readline():
    print(i)
#%% Kapa
c.close()