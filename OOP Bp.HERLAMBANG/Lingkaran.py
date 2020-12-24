class Lingkaran:
    #Koefisien Phi
    phi = 3.14

    def __init__(self,radius):
        self.radius = radius
        self.luas = 2*self.phi*radius*radius
    def keliling(self):
        return 2*self.phi*self.radius

    def Luas(self):
        return  2*self.phi*self.radius*self.radius

l1 = Lingkaran(10)

print(l1.keliling())

print(l1.luas)

