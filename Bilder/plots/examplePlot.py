import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]

x2 = [10, 20, 30]
y2 = [11, 21, 31]

plt.plot(x, y, label="First Line")
plt.plot(x2, y2, label="First Line")

plt.bar(x, y, label="Bar1", color='r')
plt.bar(x2, y2, label="Bar2", color='c')

plt.xlabel('Zeit/Jaht')
plt.ylabel('Abstraktionslevel')
plt.title("Programmierparadigmen ueber die Jahre")

plt.legend()

plt.show()
