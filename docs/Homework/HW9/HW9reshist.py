import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt

A = np.array([[6,3,1],
               [2,7,4],
               [5,1,8]],dtype=np.float64)
b = np.array([1,
               0,
               0],dtype=np.float64)

A2 = A.copy()

def Jacobi(A,b,x0,n):
    rhist = np.zeros(n)
    xold = x0
    xnew = np.zeros(np.shape(xold))
    for k in range(n):
        for j in range(len(xold)):
            total = 0
            for i in range(len(xold)):
                if i != j:
                    total += A[j,i] * xold[i]
            xnew[j] = (1/(A[j,j])) * (b[j] - total)
        # Calculate residual
        residual = b - np.dot(A,xnew)
        # Find norm and store
        normres = norm(residual)
        rhist[k] = normres
        
        xold = xnew.copy()
    return rhist

def GaussSeidel(A,b,x0,n):
    
    rhist = np.zeros(n)
    x = x0
    for k in range(n):
        for j in range(len(x)):
            total = 0
            for i in range(len(x)):
                if i != j:
                    total += A[j,i] * x[i]
            x[j] = (1/(A[j,j])) * (b[j] - total)
        # Calculate residual
        residual = b - np.dot(A,x)
        # Find norm and store
        normres = norm(residual)
        rhist[k] = normres
    return rhist

hist_J = Jacobi(A,b,np.array([1,1,1],dtype=np.float64),1000)
hist_G = GaussSeidel(A2,b,np.array([1,1,1],dtype=np.float64),1000)

# Figure 1

plt.plot(np.transpose([hist_J[:10], hist_G[:10]]),'o-',label=['Jacobi','Gauss-Seidel'])
plt.grid(True)
plt.legend()
plt.xlabel("Iteration Number")
plt.ylabel("Norm of Residual")
plt.title("Convergence of Iterative Methods")
plt.savefig("Jacobi-Gauss-1.png")
plt.close()

# Figure 2
plt.plot(np.transpose([hist_J, hist_G]),'-',label=['Jacobi','Gauss-Seidel'])
plt.grid(True)
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Iteration Number")
plt.ylabel("Norm of Residual")
plt.title("Convergence of Iterative Methods")
plt.savefig("Jacobi-Gauss-1.png")




# print("---")
# GaussSeidel(A3,b3,np.array([1,0,2],dtype=np.float64),2)
# print("---")
# Jacobi_n(A4,b3,np.array([1,0,2],dtype=np.float64),2)
# print("---")
# Jacobi(A4,b3,np.array([1,0,2],dtype=np.float64),1e-6)

