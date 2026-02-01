# VECTOR ADDITION

# Implement a program that performs element-wise addition of two vectors containing 32-bit floating point numbers on a GPU. The program should take two input vectors of equal length and produce a single output vector containing their sum.

import torch

# A, B, C are tensors on the GPU
def solve(A: torch.Tensor, B: torch.Tensor, C: torch.Tensor, N: int):
    # : is used to indicate all elements in that dimension
    C[:] = A + B
    return C
