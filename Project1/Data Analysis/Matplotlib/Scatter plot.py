from matplotlib import pyplot as plt
import random
x = [random.randint(1,100) for i in range(100)]
y = [random.randint(1,100) for i in range(100)]
plt.figure(figsize=(20,8), dpi=100)

plt.scatter(x,y)
plt.show()