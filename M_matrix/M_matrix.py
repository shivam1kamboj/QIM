# Because i index goes from 0 to N. Let's for simplicity first solve for N = 4

import numpy as np
import matplotlib.pyplot as plt

# Defining matrix M

def qim_matrix(g, N, J):

    M = np.zeros((2 * N, 2 * N + 1))

    for i, c in enumerate(M[:N]):
        c[i] = 2 * g

        c[i - 1] = -1 if i > 0 else 0
        c[i + 1] = -1 if i < N - 1 else 0

        c[N + i - 1] = -1 if i > 0 else 0
        c[N + i + 1] = -1 if i < N else 0

    for i, c in enumerate(M[N:]):
        c[N + i] = -2 * g

        c[i - 1] = 1 if i > 0 else 0
        c[i + 1] = 1 if i < N - 1 else 0

        c[N + i - 1] = 1 if i > 0 else 0
        c[N + i + 1] = 1 if i < N - 1 else 0

    return J * M[:, :-1]


# Visualising matrix M


plt.pcolormesh(qim_matrix(g=0.3, N=4, J=1), edgecolors='k', linewidth=1)
plt.title(f"M-matrix for N =4", fontsize=20)
ax = plt.gca()
ax.invert_yaxis()
ax.set_aspect('equal')
plt.colorbar()
plt.savefig('/Users/shivamkamboj/Documents/UC_Merced/Research/Spring_2023/QIM/M_matrix/M_for_N_4.pdf')


plt.pcolormesh(qim_matrix(g=0.3, N=10, J=1), edgecolors='k', linewidth=1)
plt.title(f"M-matrix for N =10", fontsize=20)
ax = plt.gca()
ax.set_aspect('equal')
plt.colorbar()
plt.savefig('/Users/shivamkamboj/Documents/UC_Merced/Research/Spring_2023/QIM/M_matrix/M_for_N_10.pdf')
