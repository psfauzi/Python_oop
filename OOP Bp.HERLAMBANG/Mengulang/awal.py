class Kulkas:

    def __init__(self,merek,harga):
        self.merek = merek
        self.harga = harga
        self.garansi = 3
        self.tenaga = 'Listrik'


Barang = Kulkas('Samsung',200)

print(f'Merek {Barang.merek}')
print(f'Harga {Barang.harga}')

Barang1 = Kulkas('LG',500)

print('\n------------')

print(f'Merek {Barang1.merek}')
print(f'Harga {Barang1.harga}')


Barang2 = Kulkas('Toshiba', 1000)

print('\n-------------')

print(f'Merek {Barang2.merek}')
print(f'Harga {Barang2.harga}')

print('\n------------')

print(f'Garansi {Barang.garansi}')
print(f'Tenaga {Barang.tenaga}')
