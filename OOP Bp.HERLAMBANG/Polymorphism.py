class Kucing:
    def __init__(self, nama):
        self.nama = nama

    def respon(self):
        return self.nama + ' Meong-meong'


class Anjing:
    def __init__(self,nama):
        self.nama = nama

    def respon(self):
        return self.nama + ' Guk-guk'


riri = Kucing('Riri')

bono = Anjing('Bono')

print(riri.respon())

print(bono.respon())

for binatang in [riri,bono]:
    print(type(binatang))
    print(binatang.respon())


    def hewan_ngomong(binatang):
        print(binatang.respon())

print(hewan_ngomong(riri))
print(hewan_ngomong(bono))

