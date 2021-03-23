#71170191
#Aprianti Vivison Wijaya
#UKDW
#referensi Modul Prak
#String

def panjangKata(a):
    kataMax = len(a[0])
    temp = a[0]
    for i in a:
        if (len(i) > kataMax):
            kataMax = len(i)
            temp = i
    print("Kata terpanjang ",temp," dengan panjang ",kataMax)

a = ["satu","ayam","goreng","mcd"]
panjangKata(a)