// LEETGPU MATRIX MULTIPLICATION (Easy)

// Write a program that multiplies two matrices of 32-bit floating point numbers on a GPU. Given matrix A of dimensions M x N and matrix B of dimensions N x K, compute the product matrix C = A x B, which will have dimensions M x K. All matrices are stored in row-major format.

#include <cuda_runtime.h>

__global__ void matrix_multiplication_kernel(const float* A, const float* B, float* C, int M, int N, int K) {
    // row and col indices for C
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    // bound check
    if (!(row < M && col < K)) {
        return;
    }
    else {
        float val = 0.0f;
        // dot product of row of A and column of B
        for (int i = 0; i < N; ++i) {
            // A is M x N and B is N x K
            val += A[row * N + i] * B[i * K + col];
        }
        C[row * K + col] = val;
    }
}

// A, B, C are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, const float* B, float* C, int M, int N, int K) {
    dim3 threadsPerBlock(16, 16);
    dim3 blocksPerGrid((K + threadsPerBlock.x - 1) / threadsPerBlock.x,
                       (M + threadsPerBlock.y - 1) / threadsPerBlock.y);
    
    matrix_multiplication_kernel<<<blocksPerGrid, threadsPerBlock>>>(A, B, C, M, N, K);
    cudaDeviceSynchronize();
}
