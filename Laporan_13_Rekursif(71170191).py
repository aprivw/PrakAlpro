#71170191 - Aprianti Vivison Wijaya - UKDW
#Rekursif
#Referensi dari modul praktikum
#Program akan menukar index 

#In = > kata yang tersusun terbalik
#Pr = > memanggil fungsi rekursif untuk menyusun dengan index
#Ou = > kata yang tersusun

def susunKata(kata):
    if kata == "":
        return kata
    else:
        return susunKata(kata[1:]) + kata[0]

isi = "nakam"
print("sebelum diganti : ", isi)
print("setelah diganti : ",susunKata(isi))
