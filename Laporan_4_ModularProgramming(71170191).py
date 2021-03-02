#71170191
#Universitas Kristen Duta Wacana
#Aprianti Vivison Wijaya
#Modular programing
#Referensi dari modul praktikum

def lingkaran(r):
    phi = 3.14
    luas = phi * (r**2)
    print(luas)

def persegi(s):
    luas = s * s
    print(luas)


def jajarGenjang(a,t):
    luas = a * t
    print(luas)

print("Mau menghitung luas apa?")
print("1.Lingkaran\n2.Persegi\n3.Jajar Genjang")
pil = input("Masukkan pilihan: ")
if pil == "1":
    r = float(input("Masukkan nilai jari-jari: "))
    lingkaran(r)
elif pil == "2":
    s = float(input("Masukkan nilai sisi: "))
    persegi(s)
elif pil == "3":
    a = float(input("Masukkan nilai alas: "))
    t = float(input("Masukkan nilai tinggi: "))
    jajarGenjang(a,t)
else:
    print("Maaf belum tersedia")
    


