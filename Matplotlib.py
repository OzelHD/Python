import matplotlib.pyplot as plt

X = range(1,10)
Y =[1, 2, 3, 1, 2, 3, 1, 2, 29]

fig = plt.figure()
ax = fig.add_subplot()


cols = ["red" if y == 2 else "blue" for y in Y]
ax.scatter(X, Y, marker = "o", c = cols)

plt.show()