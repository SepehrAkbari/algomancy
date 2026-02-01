// VECTOR ADDITION

// Implement a program that performs element-wise addition of two vectors containing 32-bit floating point numbers on a GPU. The program should take two input vectors of equal length and produce a single output vector containing their sum.

#include <cuda_runtime.h>

__global__ void vector_add(const float* A, const float* B, float* C, int N) {
    // global thread index
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    // addition within bounds
    if (idx < N) {
        C[idx] = A[idx] + B[idx];
    }
}

// A, B, C are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, const float* B, float* C, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    vector_add<<<blocksPerGrid, threadsPerBlock>>>(A, B, C, N);
    cudaDeviceSynchronize();
}