from M_matrix.M_matrix import qim_matrix
import numpy as np
import matplotlib.pyplot as plt

M = qim_matrix(g=0.3, N=10, J=1)

# Finding eigenvalues and eigenvectors of M

Eigvals, Eigvecs = np.linalg.eig(M)

D = np.diag(Eigvals)

plt.figure(figsize=(15, 10))
plt.subplot(1, 2, 1)
plt.title(f"Real Part", fontsize=20)
plt.pcolormesh(D.real, edgecolors='k', linewidth=1)
ax = plt.gca()
ax.invert_yaxis()
ax.set_aspect('equal')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title(f"Imaginary Part", fontsize=20)
plt.pcolormesh(D.imag, edgecolors='k', linewidth=1)
ax = plt.gca()
ax.invert_yaxis()
ax.set_aspect('equal')
plt.colorbar()

plt.savefig('/Users/shivamkamboj/Documents/UC_Merced/Research/Spring_2023/QIM/Matrix_diagonalization/D_matrix.pdf')

# Now defining u and u_dagger

u = Eigvecs
u_dagger = np.linalg.inv(Eigvecs)

print((M == np.around((u @ D @ u_dagger), decimals=1)).all())

plt.figure(figsize=(15, 10))
plt.subplot(1, 2, 1)
plt.title(f"M", fontsize=20)
plt.pcolormesh(M, edgecolors='k', linewidth=1)
ax = plt.gca()
ax.invert_yaxis()
ax.set_aspect('equal')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title(f"$u D u^\dagger$", fontsize=20)
plt.pcolormesh(np.around((u @ D @ u_dagger), decimals=1).real, edgecolors='k', linewidth=1)
ax = plt.gca()
ax.invert_yaxis()
ax.set_aspect('equal')
plt.colorbar()
plt.savefig('/Users/shivamkamboj/Documents/UC_Merced/Research/Spring_2023/QIM/Matrix_diagonalization/verification.pdf')
