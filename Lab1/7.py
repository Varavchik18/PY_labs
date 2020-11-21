import numpy as np
MatrixKoef = np.array( [[2,1,1],[1,2,1],[1,1,2]])
MatrixConst = np.array([2,3,-1])

result = np.linalg.solve(MatrixKoef, MatrixConst)
print("Result vector is:",result)

