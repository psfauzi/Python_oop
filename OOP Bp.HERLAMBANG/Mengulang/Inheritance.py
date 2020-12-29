class Mahasiswa:

    status = 'Mahasiswa'

    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def keterangan(self):
        return '{} Dikelas {} adalah Seorang {}'.format(self.nama,self.kelas,self.status)

class Nilai(Mahasiswa):

    def __init__(self,nama, kelas):
        super().__init__(nama,kelas)
        self.nilai_update = []

    def input_nilai(self,tambah):
        return self.nilai_update.append(tambah)

Mhs = Mahasiswa('Fauzi Bariq Mahya',3)

print(f'{Mhs.keterangan()}')
print('\n--------------')

Mhs = Nilai('Fauzi Bariq Mahya',12)
print(Mhs.input_nilai(58))
print(Mhs.nilai_update)