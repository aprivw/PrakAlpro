#71170191 - Aprianti Vivison Wijaya - UKDW
#List
#Referensi dari modul praktikum
#Program akan menukar posisi list yang di inputkan

#In = > posisi list pertama, posiso list yang ditukar
#Pr = > buat sebuah list yang berisi angka -> meminta inputan pos1,pos2 ->memanggil fungsi gantiPosisi yang akan menukar list tersebut
#Ou = > sebuat list yang posisi isinya dalamnya sudah tertukar dari inputan posisi list awal 

def gantiPosisi(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

List= [23, 65, 19, 90]
pos1 = int(input("Masukkan posisi 1: "))
pos2 = int(input("Masukkan posisi 2: "))
print("Posisi list sebelum diubah: ", List)
print("Posisi list setelah diubah: ", gantiPosisi(List, pos1-1, pos2-1))
