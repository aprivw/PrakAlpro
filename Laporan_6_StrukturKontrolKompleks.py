#71170191
#Ukdw
#Struktur Kontrol Kompleks
#referensi modul praktikum

total_harga = 0
kuota_A = 3
kuota_B = 5
kuota_C = 2

while(True):
    print("Sepatu yang tersedia")
    print("1.Sepatu A [Rp.130.000,-]")
    print("2.Sepatu B [Rp.200.000,-]")
    print("3.Sepatu C [Rp.250.000,-]")
    print("4.Bayar")
    print("Pembelanjaan diatas Rp.500.000 mendapatkan diskon sebesar 5%")
    pil = input("Masukkan pilihan: ")
    if pil == "1":
        if kuota_A > 0:
            total_harga+=130000
            kuota_A-=1
            print("Sepatu A sudah ditambahkan")
        else:
            print("Sepatu A sudah habis !")
    elif pil == "2":
        if kuota_B > 0:
            total_harga+=200000
            kuota_B-=1
            print("Sepatu B sudah ditambahkan")
        else:
            print("Sepatu B sudah habis !")
    elif pil == "3":
        if kuota_C > 0:
            total_harga+=250000
            kuota_C-=1
            print("Sepatu C sudah ditambahkan")
        else:
            print("Sepatu C sudah habis !")
    elif pil == "4":
        break
    else:
        print("Menu tidak tersedia")

uang = float(input("Masukkan jumlah uang: "))

if total_harga >= 500000:
    print("kamu mendapatkan diskon 5%")
    diskon = total_harga * 5/100
    bayar = total_harga - diskon
else:
    bayar = total_harga

total = uang - bayar

print("Jumlah uang anda: Rp.",uang)
print("Total yang harus dibayar Rp.",bayar)
print("Kembalian : ",total)
print("Terimakasih sudah berbelanja")

    

