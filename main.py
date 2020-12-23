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