#try catch methodu
olanVar=5
olanVar2=4
#BÝ sýkýntý çýkana kadar aþþaðdaki 
#eylemi gerçekleþtir:
try:
    print(olanVar+olmayanVar)
#Baktýn sýkýntý çýkýyo, buradan devam (pass) et
except:
    pass
print("geçtim")

'''
except ValueError:
    print("bla bla") 
gibi ya da
(#Çýkan error NameError mü diye bak)
except NameError as error:
#geri kalan ne varsa
except Exception as error:
#'da çoðul hali
#hiçbiri olmadý buraya bi
else:   '''

#SETLER




