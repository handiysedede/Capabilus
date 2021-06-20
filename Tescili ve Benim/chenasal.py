#%%
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    
    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    i = 5
    while(i*i<= n):
        if (n % i == 0 or n % (i+ 2)==0):
            return False
        i = i + 6
    return True
#%%
def fact(asal_sayi=int(input("-->"))):
    if asal_sayi>1 and asal_sayi!=2:
        for i in range(2,asal_sayi):
            if (asal_sayi % i)==0:
                print(asal_sayi," asal değil kardeş")
                break
            else:
                print(asal_sayi," asal kardeş")
                break
    else:
        terk= print(asal_sayi, ' asal değil kardeş')
        return terk
#%%
if (isPrime(11)):
    print("true")
else:
    print("false")
#%%
if(isPrime(15)):
    print("true")
else:
     print("false")
#%%
chen=isPrime(int(input("bana bi sayı ber ")))
if chen and fact(chen+2)==isPrime() is True:
    print("OHA")
        