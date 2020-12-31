class Coba:
    def __init__(self,nama,angka, kata):
        self.nama = nama
        self.angka = angka
        self.kata = kata
    def cetak(self):
        return self.nama

    def __str__(self):
        return self.nama

    def __len__(self):
        return 1000

coba = Coba('Fauzi',20,'Ganteng')

print(coba.cetak())

print(dir(coba))

print(coba.__str__())

print(str(coba))

print(len(coba))