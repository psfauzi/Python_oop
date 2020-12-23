class Rumah:

    def __init__(self,merek,harga):
        self.merek = merek
        self.harga = harga
        self.garansi = 3
        self.kontruksi = 'Batu Bata Super'

barang1 = Rumah('Minimalis',500)

print(f'Merek Rumah {barang1.merek}')
print(f'Harga Rumah {barang1.harga}')

print('\n------------------------')


barang2 = Rumah('Tingkat',1000)

print(f'Merek Rumah {barang2.merek}')
print(f'Harga Rumah {barang2.harga}')

print('\n------------------------')

print('\n',barang2.garansi)
print(barang2.kontruksi)