class Handphone:


    penjual = 'Fauzi Bariq Mahya'

    def __init__(self, merek,harga):
        self.merek = merek
        self.harga = harga
        self.garansi = 5
        self.tenaga = 'Baterai'

    def Keterangan(self,anak):
        return 'kulkas merek {} harganya sebesar {} nama penjualnya {} yang punya anak {}'.format(self.merek, self.harga, self.penjual, anak)


Beli = Handphone('Samsung',50000)

print(f'Nama Penjualnya {Beli.penjual}')

print(Beli.Keterangan(5))