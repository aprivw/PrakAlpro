#71170191 - Aprianti Vivison Wijaya - UKDW
#Dictionary
#Referensi dari modul praktikum
#Program akan menghitung total belanjaan berdasarkan input dari user

#In = > Pilihan buah yang dipilih, jumlah buah
#Pr = > berdasarkan pilihan buah dari user maka akan mengakses nilai sesuai value didict, 
# kemudian akan menambahkan di list nota yang akhirnya nanti akan mencetak total belanja
#Ou = > Total belanja dari user

dictBuah={
    'apel' : 5000,
    'kiwi' : 7000,
    'jambu': 3000
}

listNota=[]

while(True):
    print("======Selamat datang ditoko buah=======")
    print("Masukkan buah apa yang dibeli: ")
    print("1.Apel")
    print("2.Kiwi")
    print("3.Jambu")
    print("4.Total")
    print("5.Keluar")
    pil = input("Masukkan pilihan: ")
    if pil == "1":
        jml1 = int(input("Masukkan jumlah buah: "))
        harga = dictBuah['apel'] * jml1
        listNota.append(harga)
        print(harga)
    elif pil == "2":
        jml2 = int(input("Masukkan jumlah buah: "))
        harga1 =dictBuah['kiwi'] * jml2
        listNota.append(harga1)
        print(harga1)
    elif pil == "3":
        jml3 = int(input("Masukkan jumlah buah: "))
        harga2 = dictBuah['jambu'] * jml3
        listNota.append(harga2)
        print(harga2)
    elif pil == "4":
        print("Total Belanja : ", sum(listNota))
        break
    elif pil == "5":
        break
    else:
        print("Maaf input salah")


