import numpy as np
m = np.array([[1,-2,3],[1,4,-12]])
print(np.transpose(m))
print('-----------------------')

#resolver sistemas de ecuaciones
a = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b = np.array([[-3],[5],[-2]])
x = np.linalg.solve(a,b)
print(x)
#verificar
print(np.allclose(np.dot(a,x),b))