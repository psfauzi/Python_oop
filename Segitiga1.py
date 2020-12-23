class Segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def info(self):
        return f'Ini adalah Objek dari Luas Segitiga {self.alas} dan Lebar {self.tinggi}'

    def hitung_luas(self):
        return self.alas * self.tinggi