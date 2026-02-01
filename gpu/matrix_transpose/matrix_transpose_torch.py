# MATRIX TRANSPOSE

# Write a program that transposes a matrix of 32-bit floating point numbers on a GPU. The transpose of a matrix switches its rows and columns. Given a matrix, A, of dimensions (rows, cols), the transpose, A^T, will have dimensions (cols, rows). All matrices are stored in row-major format.

import torch

# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, rows: int, cols: int):
    output[:] = input.t()
    return output