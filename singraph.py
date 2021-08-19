import matplotlib.pyplot as plt
import math
x = [1, 2, 3, 4, 5]
y = [math.sin(1), math.sin(2), math.sin(3), math.sin(4), math.sin(5)]
plt.title("Sin num vs num")
plt.xlabel("Num")
plt.ylabel("Sin num")
plt.plot(x, y, color = "red", marker = "x")
plt.show()