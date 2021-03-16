#71170191
#Struktur Kontrol Percabangan
awal = int(input("Masukkan saldo awal: "))
sisa = awal
while (sisa > 0):
    pengeluaran = int(input("Masukkan pengeluaran: "))
    if pengeluaran <= -1: 
        print("Sisa saldo", sisa,"\nPengeluaran tidak boleh negatif")
        break
    elif pengeluaran >-1:
        sisa  = sisa - pengeluaran
        print("sisa saldo: ",sisa)
if awal==0:
    print("Saldo awal masih 0, tambah gan")
elif sisa == 0:
    print("Saldo habis gan, berhenti belanja")
elif sisa > 0:
    print("Masih ada saldo gan, belanja lagi")
