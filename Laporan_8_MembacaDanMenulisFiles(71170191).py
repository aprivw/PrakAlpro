#71170191 - Aprianti Vivison Wijaya - UKDW
#Files - Membaca dan menulis files
#Referensi dari modul praktikum
#Program akan menyimpan dan menampilkan catatan pengeluaran dari setiap bulan, diakhir juga akan menghitung semua total pengeluaran

#In = > bulan,jmlBelanja, namaBrang,hargaBrang
#Pr = > meminta inputan dari user, kemudian menyalin di file bulanan.txt, kemudian menampilkan dari membaca data di file bulanan.txt
#Ou = > Catatan yang berisi bulan,nama barang, harga barang, serta total pengeluaran

cek = True
while(cek):
    print("--Catatan Bulanan--")
    print("1.Tambah Catatan")
    print("2.Lihat Catatan")
    print("3.Keluar")
    pil=int(input("Pilihan: "))
    if pil==1:
        dataW=open('bulanan.txt','a')
        print("--Tambah Data Belanja Bulanan--")
        bln=input("Catatan untuk bulan: ")
        jmlB=int(input("Masukkan jumlah barang belanjaan: "))
        for i in range(jmlB):
            namaB = input("Masukkan nama barang: ")
            hargaB = int(input("Masukkan harga barang: "))
            dataW.write(bln+","+namaB+","+str(hargaB))
            dataW.write("\n")
        print("Catatan berhasil disimpan\n")
        dataW.close()
    elif pil==2:
        print("--List Belanja Bulanan--")
        dataR=open('bulanan.txt','r')
        baris=dataR.readlines()
        tot=0
        print("Bulan \tNama Barang\t Harga barang")
        print("---------------------------------------")
        for i in baris:
            tamp = i
            b,nm,hg = tamp.split(",",3)
            print(" "+b+" \t"+nm+"\t \t\t"+hg)
            t = (int(hg))
            tot +=t
        dataR.close()
        print("---------------------------------------")
        print(" \tTotal Pengeluaran:\t",tot)
        print("\n\n")
    elif pil==3:
        print("Keluar dari program....")
        cek = False
    else:
        print("Inputan tidak tersedia")
