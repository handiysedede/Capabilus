##
a = 1
b =2
if a<b:
    print("a b'den küçüktür")
    print("a kesin b'den küçüktür")
print("bilemedim şimdi")
##
c = 3
d = 4
if c <d:
    print("c d'den küçüktür")
else:
    print("c d'den KESİN küçük değildir")
    print("sanmam yani")
print("çıktık iften")
##
e=3
f=40
if e<f:
    print("e f'den küçüktür")
elif e==f:
    print("e f'ye eşittir")
elif f< e +10:
    print("sen e'ye 10 koy f yine büyüktür")
else:
    print("e f'den küçük falan değil kardeşim")
##    
g=85
h=8
if g<h:
    print("g<h")
else:
    if g==h:
        print("g : h")
    else:
        print("g aşmış yürümüş")
##

def your_choise(answer):
    if answer >5:
        print(" çok büyük yannız sizin yaşınız")
    elif answer<= 5 and answer >2:
        print('analar kreşine hoşgeldiniz')
    elif answer == 2:
        print('ooooo buyrun buyrun ')
    else:
        print('yok artık')


print(your_choise(4))

i=0
while True:
    i=i+1
    if i==5:
        print("beşi geçtim")
        continue
    if i==10:
        print("onu geçtim")
        continue
    if i==19:
        print("yeter di mi ?")
        break
    print(i)
print("afferin LAAAAAN")
