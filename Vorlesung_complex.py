import math as m

class Complex:
    def __init__(self, re, im):
        self.real = re
        self.imag = im

        self.r = m.sqrt(re**2 + im**2)  #Transformation in Polarkoordinaten
        self.th = m.atan(im/re)         #Transformation in Polarkoordinaten


    def modulus(self):
        return m.sqrt(self.real ** 2 + self.imag ** 2)
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __mul__(self, other):
        return Complex(self.real * other.real, self.imag * other.imag)
    # def __truediv__(self, other):
    #     return Complex(self.real / other.real, self.imag / other.imag)

    def __truediv__(self, other):    #mit Polarkoordinaten
        new_r = self.r / other.r
        new_th = self.th - other.th
        new_real = new_r * m.cos(new_th)
        new_imag = new_r * m.sin(new_th)
        return Complex(new_real, new_imag)
    
    def pretty_print(self):
        print(f"{str(self.imag)} + {str(self.real)}i")