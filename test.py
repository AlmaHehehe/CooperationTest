import numpy as np
a = np.random.randint(1, 3, (2,3))
print(a)
print('This is a cooperation test')
b = np.random.randint(3, (2,3))

c = a.T @ b
print(c)
