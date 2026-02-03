'''
Linear Layer Forward Pass.
'''

def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    Y = [[0.0 for _ in range(len(W[0]))] for _ in range(len(X))]
    
    for i in range(len(X)):
        for j in range(len(W[0])):
            sum = 0.0
            for k in range(len(W)):
                sum += X[i][k] * W[k][j]
            Y[i][j] = sum + b[j]
    
    return Y


if __name__ == "__main__":
    X = [[1, 2], [3, 4]]
    W = [[1, 0], [0, 1]]
    b = [0, 0]
    print(linear_layer_forward(X, W, b))