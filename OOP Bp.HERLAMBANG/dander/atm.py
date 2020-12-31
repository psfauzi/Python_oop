class RekeningBank:

    def __init__(self,tabungan):
        self.tabungan = tabungan

    def cek_saldo(self):
        return 'Saldo anda adalah = Rp. {}'.format(self.tabungan)


    def menabung(self):
        self.tambah = int(input('Masukkan uang tabungan anda = Rp.' ))
        self.tabungan = (self.tabungan + self.tambah)

    def tarik_saldo(self):
        self.tarik = int(input('Mau narik berapa saldo =? Rp.'))
        if self.tabungan < self.tarik:
            return 'Uang anda tidak mencukupi'
        else :
            return 'Sisa saldo anda adalah {}'.format(self.tabungan-self.tarik)


bri = RekeningBank(1000)


print(bri.menabung())
print(bri.cek_saldo())

print(bri.tarik_saldo())