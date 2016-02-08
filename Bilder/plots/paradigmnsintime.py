import matplotlib.pyplot as plt

x = [1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
plt.scatter(x, y, s=2)
plt.xlabel('Zeit/Jahr')
plt.ylabel('Abstraktionslevel')
plt.title("Programmierparadigmen ueber die Jahre")

plt.legend()

plt.show()
