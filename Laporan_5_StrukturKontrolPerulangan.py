#71170191
#Struktur Kontrol Percabangan
awal = int(input("Masukkan saldo awal: "))
sisa = awal
while (sisa > 0):
    pengeluaran = int(input("Masukkan pengeluaran: "))
    if pengeluaran == -1:
        print("sisa saldo", sisa)
    elif pengeluaran >-1:
        sisa = sisa - pengeluaran
        print("sisa saldo: ", sisa)
print("saldo habis gan, berhenti belanja")
    
