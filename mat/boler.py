#Bebe gibi böler bu program
def bol():
    bolunen = float(input("Neyi: "))
    bolen = float(input("Neyle bölelim ? : "))
    kalan=float(bolunen%bolen)
    bolum=float(bolunen/bolen)
    sonuc = print("Bölünen: " , float(bolunen), "\nBölen:    " , float(bolen),"\nBölüm:    ", float(bolum),  "\nKalan:    ", float(kalan))
    """if kalan<=bolen:
        print("Güzel bir bölüm oldu...")
    else kalan<=bolum:
        bolen==bolum
        bolum==bolen
        print("Olanlar oldu, kalan:",kalan,)"""
    return sonuc
bol()



