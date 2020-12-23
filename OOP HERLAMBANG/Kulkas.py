class Kulkas:

    def __init__(self,merek,harga):
        self.merek = merek
        self.harga = harga
        self.garansi = 3
        self.tenaga = 'Listrik'

barang1 = Kulkas('samsung',500)

print(barang1.merek)
print(barang1.harga)

barang2 = Kulkas('Toshiba',1200)
print('\n----------')
print(barang2.merek)
print(barang2.harga)


print('\n----------')

barang3 = Kulkas('LG',1200)
print(barang3.merek)
print(barang3.harga)

print('\nRincian')
print(barang3.garansi)
print(barang3.tenaga)