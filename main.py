from Persegi1 import PersegiPanjang
from Segitiga1 import Segitiga
print('Belajar OOPS')

def info():
    return 'Modul menghitung rumus-rumus tentang segitiga'

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

p1 = PersegiPanjang(10,5)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(10,3)
print(s1.info())
print(s1.hitung_luas())

print('\nMencoba Membuat Objek dari Kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

#Molymorpishm : Kemampuan Objek untuk merespon berbeda, terhadap pemanggilan method yang sama

daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())