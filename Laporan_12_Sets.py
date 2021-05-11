#71170191 - Aprianti Vivison Wijaya - UKDW
#Set
#Referensi dari modul praktikum
#Program akan mengeluarkan output angka yang tidak ada di set

#In = > Set yang berisi angka, low sebagai angka terendah, high sebagai angka tertinggi
#Pr = > akan membaca set, kemudian var low dan high, melakukan looping denga low dan high, 
#       jika angka tidak ada dari lopping maka akan disimpan di list tamp
#Ou = > angka yang tidak ada di set.

nilaiSet = {6,4,2,7,9}

print("Original set berisi : " + str(nilaiSet))

low = 5
high = 10

tempList = []
for i in range(low,high+1):
    if i not in nilaiSet:
        tempList.append(i)

print("Elemen yang tidak ada didalam set adalah: " + str(tempList))
