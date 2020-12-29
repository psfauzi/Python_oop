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


class Lingkaran:

    phi = 3.14

    def __init__(self,radius):
        self.radius = radius
        self.luas =  2*self.phi*self.radius*self.radius

    def keliling(self):
        return 2*self.phi*self.radius

l1 = Lingkaran(10)

print(f'Luas dari {l1.radius} adalah {l1.luas}')

print(f'Keliling dari {l1.radius} adalah {l1.keliling()} ')