from Vorlesung_complex import Complex as C

a = C(1, 2) #1+2i
b = C(3, 4)

print(f"{a.modulus()} a.modulus")
print(f"{b.modulus()} b.modulus")
print(f"{(a + b).modulus()} (a+b).modulus")
print(f"{(a - b).modulus()} (a-b).modulus")
print(f"{(a * b).modulus()} (a*b).modulus")
print(f"{(a / b).modulus()} (a/b).modulus")
c = a*b
d = a/b




a.pretty_print()
b.pretty_print()
c.pretty_print()
d.pretty_print()


