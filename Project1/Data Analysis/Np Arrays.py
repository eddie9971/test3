import numpy as np

a = np.array([1,2,3,4,5])
b = np.array((1,2,3,4,5))
c = np.array(range(10))
d = np.array([i**2 for i in range(10)])
e = np.array([i for i in range(10) if i%2 == 0])
f = np.array([1,2,3.14,4,5])
g = np.array([
    [1,2,3],
    ('a','b','c')
])
a1 = np.array([1,2,3,4,5], dtype='float')
h = np.array([1.1,2.6,3.4,4.5,5.9], dtype='int')
i = np.arange(3.1) #range cant take float
j = np.arange(10,dtype='float')
k = np.linspace(1,10,10,dtype='int')
k1 = np.linspace(0,4,9)
l = np.logspace(0,9,10,base=2)
l1 = np.logspace(1.0,2.0,num=10) #default base=10
n = np.zeros(4)
n1 = np.zeros((3,4))
m = np.random.rand(5) #distribution from 0 to 1 for two demensional (5,5)
m1 = np.random.randn(2) # normal distribution -1 to 1
o = np.arange(25).reshape(5,5)
o1 = np.random.randint(0, 50, 10).max()
o2 = np.random.randint(0, 50, 10).argmin()
p = np.arange(1,11)
p1 = p > 5
p2 = p[p1]
p3 = p[p<3]
p4 = p + 100
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')
print(f'd: {d}')
print(f'e: {e}')
print(f'f: {f}')
print(f'g: {g}')
print(f'a1: {a1}')
print(f'h: {h}')
print(f'i :{i}')
print(f'j: {j}')
print(f'k: {k}')
print(f'k1" {k1}')
print(f'l: {l}')
print(f'l1: {l1}')
print(f'n: {n}')
print(f'n1: {n1}')
print(f'm: {m}')
print(f'm1 {m1}')
print(f'o: {o}')
print(f'o1: {o1}')
print(f'o2: {o2}')
print(f'p1: {p1} | {p2}')
print(f'p3: {p3}')
print(f'p4: {p4}')