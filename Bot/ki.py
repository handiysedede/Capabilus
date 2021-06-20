n=5
for x in list(range(n)) +list(reversed(range(n-1))):
    a = n-x-1
    b = x*2+1
    print('{: <{w1}}{:*<{w2}}'.format('','',w1=a, w2=b))
#%%
import time
print("ENTER'la başlasın")
print("Cntrl+C'le de dursun amk..")

while True:
    try:
        input()
        start_time=time.time()
        print("Başladı, koş !!!")
    except KeyboardInterrupt:
        print("Hoşt!!")
        end_time = time.time()
        print(round(end_time - start_time, 3), "saniye geçti...")
        break
#%%
