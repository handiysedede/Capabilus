try:
    inputFile= open("C:\py\coz\Dene, olursa sen/bıcdır.txt", encoding="utf-8")
    for line in inputFile:
        print(line)
    inputFile.close()
except (IOError,UnicodeDecodeError) as error:
    print("IOError oldu yaa")