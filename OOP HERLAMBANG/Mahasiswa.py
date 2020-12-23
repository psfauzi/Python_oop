#Inheritance

class Mahasiswa:

    status = 'mahasiswa'

    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def keterangan(self):
        print('{} di kelas {} adalah seorang {}'.format(self.nama,self.kelas,self.status))


mhs = Mahasiswa('Joko',12)

print(mhs.keterangan())

class Nilai(Mahasiswa):

    def __init__(self, nama, kelas):
        super().__init__(nama,kelas) # Mahasiswa  __init__(nama, kelas)
        self.nilai_update = []

    def input_nilai(self,tambah):
        return self.nilai_update.append(tambah)

budi = Nilai('Budi',13)

print(budi.keterangan())

budi.input_nilai(85)

print(budi.nilai_update)