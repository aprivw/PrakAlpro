print("Selamat datang di toko buah")
print("1.Pilih buah")
print("2.Exit")
harga = 0
uang = 0
pil = input("Masukkan pilihan : ")
if pil == "1":
    apel = 13000
    kiwi = 15000
    semangka = 20000
    print ("1.Apel 13.000/kg")
    print ("2.Kiwi 15.000/kg")
    print ("3.Semangka 20000/kg")
    pil_buah = input("Masukkan pilihan: ")
    jml_buah =int(input("Masukkan berapa kg yang akan dibeli: "))
    uang = float(input("Masukkan uang anda: "))
    if pil_buah == "1":
        harga = jml_buah * apel
        total = uang - harga
        print("================================================")
        print("Anda membeli ",jml_buah," kg apel seharga ",harga)
        print("Jumlah uang anda : ",uang)
        print("Kembalian anda : ",total)
        print("================================================")

    elif pil_buah == "2":
        harga = jml_buah * kiwi
        total = uang - harga
        print("================================================")
        print("Anda membeli ",jml_buah," kg kiwi seharga ",harga)
        print("Jumlah uang anda : ",uang)
        print("Kembalian anda : ",total)
        print("================================================")
    elif pil_buah == "3":
        harga = jml_buah * semangka
        total = uang - harga
        print("====================================================")
        print("Anda membeli ",jml_buah," kg semangka seharga ",harga)
        print("Jumlah uang anda : ",uang)
        print("Kembalian anda : ",total)
        print("====================================================")
    else:
        print("Pilihan tidak ada")
elif pil =="2":
    print("Keluar dari program")
    
else:
    print("Tidak ada pilihan tersebut")