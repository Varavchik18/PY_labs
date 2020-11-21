import numpy as np
MatrixA = np.matrix( "1,1,-2,1,3; -1,2,1,-1,-2; 3,0,2,1,-1; 3,3,1,1,-1" )

print("Initial Matrix:\n",MatrixA)

rank = np.linalg.matrix_rank(MatrixA)

print("\n")
print("Matrix rank is:\n",rank)
