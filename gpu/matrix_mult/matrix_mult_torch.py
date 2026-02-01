# MATRIX MULTIPLICATION

# Write a program that multiplies two matrices of 32-bit floating point numbers on a GPU. Given matrix A of dimensions M x N and matrix B of dimensions N x K, compute the product matrix C = A x B, which will have dimensions M x K. All matrices are stored in row-major format.

import torch

# A, B, C are tensors on the GPU
def solve(A: torch.Tensor, B: torch.Tensor, C: torch.Tensor, M: int, N: int, K: int):
    C[:] = torch.mm(A, B)
    return C