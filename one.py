hesapSahibi=str("Utku")
bakiye=int(100)


kartSahibi=str("TUtku")
işlem=int(20)
güvenilirSatıcılar=["dayı","adam","biri"]
satıcı="dayı"

if işlem<bakiye:
    if hesapSahibi==kartSahibi:
        if satıcı in güvenilirSatıcılar:
            print(bakiye-işlem)
            print("işlem gerçekleşti. Kalan bakiyeniz", bakiye)
        else:
             print("bu satıcıya güven olmaz")
    else:
         print("kart sahibi sen misin harbi?")
else:
    print("FAKİİİİR")