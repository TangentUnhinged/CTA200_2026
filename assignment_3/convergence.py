import numpy as np

def convergence(c, max_iter = 10, radius = 2.0):
    z = np.zeros(c.shape, dtype = complex)
    diverge_at = np.zeros(c.shape)
    
    for n in range(max_iter):
        conv = np.abs(z) < radius
        z[conv] = np.square(z[conv]) + c[conv]
        diverge_at[conv] += 1
        
    return diverge_at