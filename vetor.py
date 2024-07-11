# Anteriormente, NÃO foi o resultado esperado com multiplicação vetorial por um escalar

# É preciso fazer isto
print([i*3 for i in [1,2,3]])

# Soma de dois vetores
a = [1,2,3]
b = [4,5,6]
print([a[i] + b[i] for i in range(len(a))])

# Poderíamos calcular o produto escalar assim: 

u = [1,2,3]
v = [4,5,6]

total = 0 
for i in range(len(u)):
    total += u[i] * v[i]
print(total)

# Vamos ver o que acontece se usarmos Numpy

# np é uma convenção comum para se referir a Numpy ao longo de todo o código
import numpy as np 
u = np.array([1,2,3])
v = np.array([4,5,6])
# dot() calcula o produto escalar de dois vetores
print(np.dot(u,v))
print(type(u))
print(u)

# Mais algumas operações em matrizes 1D:

import numpy as np
u = np.array([1,2,3])
v = np.array([4,5,6])

print("Vector addition with another vector ---> " + str(u+v))
print("Vector addition with a scalar ---> " + str(u+4))
print("Vector multiplication by a scalar ---> " + str(u * 4))
print("Vector multiplication (NOT dot nor cross product) ---> " + str(u * v))
print("Vector sum ---> " + str(np.sum(u * v)))
print("Dot product ---> " + str(np.dot(u,v)))