class Kulkas1:
    #class object attribute (atribute ini bersifat global untuk class kulkas)
    penjual = 'Pak Mamat'

    def __init__(self,merek,harga):
        self.merek = merek
        self.harga = harga
        self.garansi = 3
        self.kontruksi = 'Batu Bata Super'

    def konsumsi(self):
        print('500 watt')

    def keterangan(self,anak=5):
        print('Kulkas Merek {} harganya sebesar {} dan nama penjualnya {} yang punya anak {}'.format(self.merek,self.harga,self.penjual,anak))

Barang = Kulkas1('LG',5000)

print(Barang.penjual)

print(Barang.keterangan(6))