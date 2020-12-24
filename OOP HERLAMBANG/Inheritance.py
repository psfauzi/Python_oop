class Mahasiswa:

    status = 'Mahasiswa Tampan Insyaallah'

    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def keterangan(self):
        print('{} dikelas {} adalah Seorang {}'.format(self.nama,self.kelas,self.status))

Fauzi = Mahasiswa('Fauzi Bariq Mahya', 12)

print(Fauzi.keterangan())


class Nilai(Mahasiswa):
    def __init__(self,nama,kelas):
        super().__init__(nama,kelas) # Mahasiswa .__init__(kelas,nama)
        self.nilai_update = []

    def input_nilai(self,tambah):
        return self.nilai_update.append(tambah)

budi = Nilai('Ganteng',12)

print(budi.keterangan()) #Cetak dari Pewarisan Atau Inheritance

print(budi.input_nilai(80))
print(budi.nilai_update)