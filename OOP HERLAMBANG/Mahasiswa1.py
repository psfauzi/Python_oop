class Kulkas:

    # class Object Atrribute (attribute ini bersifat global untuk class kulkas)
    penjual = 'Fauzi Bariq Mahya'

    def __init__(self, merek, harga):
        self.merek = merek
        self.harga = harga
        self.garansi = 3
        self.tenaga = 'Listrik'

    def keterangan(self, anak=5):
        print('Kulkas Merek {}  Harganya Sebesar {} Nama Penjualnya {} Yang punya anak {}'.format(self.merek,self.harga,self.penjual,anak))

barang = Kulkas('Iphone',1500)

print('Nama Pembeli :', barang.penjual)
print(barang.keterangan())

print('\nClass Lingkaran Inheritance')
class Lingkaran:

    phi = 3.14
     #koefisien phi

    def __init__(self,radius):
        self.radius = radius
        self.Luas = 2*self.phi*self.radius*self.radius # Menghitung Luas  di dalam init

    def keliling(self):
        return 2*self.phi*self.radius

    # def Luas(self): #Menghitug luas dengan Message Baru /method fungsi
    #     return 2*self.phi*self.radius*self.radius

l1 = Lingkaran(10)

print('Ini adalah keliling dari :',l1.radius, '=' ,  l1.keliling())

print('Ini adalah Luas dari', l1.radius ,'=',l1.Luas)



