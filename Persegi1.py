class PersegiPanjang():
    def __init__(self,p,l):
        self.p = p
        self.l = l
    #Fungsi yang dipanggil pertama kali
    def info(self):
        return f'Ini adalah Objek dari Luas PErsegi Panjang {self.p} dan Lebar {self.l}'

    def hitung_luas(self):
        return self.p * self.l