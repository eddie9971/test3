from matplotlib import pyplot as plt

x = ['a', 'b', 'c', 'd', 'e']
y = [96,54,76,58,98]
y2 = [32,65,23,76,45]
y3 = [12,54,7,23,87,54]

xx = list(range(len(x)))
x1 = [i+0.2 for i in xx]
x2 = [i+0.2*2 for i in xx]
print(x1)
plt.bar(x,y,width=0.2)
plt.bar(x1,y2,width=0.2)
plt.bar(x2,y3)
plt.show()