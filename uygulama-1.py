#0'dan 1'e kadar sayıları bir text dosyasına yazdırınız
dosya=open("sayılar.txt","w")
for i in range(0,2):
    dosya.write(str(i)+"\n")
dosya.close()