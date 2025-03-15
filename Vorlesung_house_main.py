from Vorlesung_house import House as H
from Vorlesung_house import Tower as T
from Vorlesung_house import Castle as C

h1 = H(1990, 'Budapester Str. 9', (3, 4), 7, 10)
h2 = H(1985, "Apfelstr 129", (4, 6), 6, 10)
t = T(2000, 'Potsdamer Platz 1', 5, 5)
d = C(1800, "Apfelstr 456", (-4, -10), 10, 20, 4)


city = [h1, h2, t, d]


print(f"{sum([x.area() for x in city])} is the Housing area of the city")
print(f"Hello {h1.age()} age of d, {h1.address} Adresse of d. Bye.")