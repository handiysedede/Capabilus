import time
import sys
import datetime
import locale
import random
locale.setlocale(locale.LC_ALL, '')
kullanici_adi=str("utku")
sifre=str("****")
negle="İlgilenmiyorum"
fak=["f","F","siktir","Siktir","ff","FF"]
kapa="Pekala, zaman ayırdığınız için teşekkür ederim. Sizlere iyi günler dilerim."
#%%
class call():
    def __init__(self, name):
        self.name = name
    def robotmu():
        """if input("Bakalım robot musun? \n(2+2)4*0= ") != str(0):
            sys.exit("Robotsun di mi sen? ")
        else:"""
            print("Pekala..")
            print("----%----")
            s = time.strftime("%d %b %Y %H:%M:%S ,%A")
            return s
    time.sleep(2)
    #%%
    def giris():
        load=1
        if input("Kullanıcı adı:  ") == kullanici_adi and input("Şifre:  ") == sifre:
            while load<5:
                print("\rSisteme giriş yapılınıyor"+ ("."* load), end=" ")
                time.sleep(1)
                load+=1
            return "\nMerhaba " + kullanici_adi + " ! İyi çalışmalar!"
        else:
            print("Sen de kimsin ? --Yabancı algılandı--")
            sys.exit("Terket burayı !!!! ")
    #%%
    def selam():       
        print("İyi günler, iyi akşamlar, merhabalar")
        time.sleep(2)
        print("Sizi Digitürk'den arıyorum. ")
        time.sleep(3)
        return time.strftime("%B") + " ayına özel fırsatlar hakkında bilgi aktarmak amacı ile sizlere ulaşım sağlamaktayım."
    def sunum():
        time.sleep(2)
        if input() in fak:
            print("Fiyatlarımızı dinlemenizi öneririm")
            #Buraya bişeyler gelicek
        elif input()=="var":
            print("Evde ki bütün televizyonlarda var mı?\nİkinci televizyona aynı paketinizin yarı fiyatına kurulum yapabilirim.")
            #Buraya bişeyler gelicek
        else:
            time.sleep(3)
            print("İlgilenir miydiniz?")
        if input(negle+" ") in fak:
            time.sleep(2)
            print("Başka bir uydu platformu mu kullanmaktasınız?")
            if input() in fak:
                print("Şu anda bağlı olduğunuz taahütden memnun musunuz?\nDeğilseniz fiyatlarımız dinlemenizi öneririm...")
                #Buraya bişeyler gelicek
                time.sleep(6)
        return kapa
print(call.sunum())
#%%
print(call.robotmu())
print(call.giris())
print(call.selam())
print(call.sunum()) 

#%%    
