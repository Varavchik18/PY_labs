import numpy as np
ArrayA = np.array(
    [[4,3],[1,1]])

ArrayB = np.array(
    [[2,8],[1,1],[0,-1]])

print("\n")
print("Array A:\n", ArrayA)
print("Array B:\n", ArrayB)

X = np.dot(ArrayB, np.linalg.inv(ArrayA))
print("Matrix X=\n", X)

#print(np.dot(X,np.linalg.inv(ArrayA)))