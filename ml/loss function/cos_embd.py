'''
Cosine Embedding Loss.
'''

from cProfile import label
import math

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    x1_norm = math.sqrt(sum(i*i for i in x1))
    x2_norm = math.sqrt(sum(i*i for i in x2))

    if x1_norm == 0 or x2_norm == 0:
        cos_sim = 0.0
    else:
        prod = sum(i*j for i,j in zip(x1,x2))
        prod_norm = x1_norm * x2_norm

        cos_sim = prod / prod_norm

    if label == 1:
        return 1 - cos_sim
    elif label == -1:
        return max(0, cos_sim - margin)
    else:
        raise ValueError
    
    
if __name__ == "__main__":
    x1 = [1, 0, 0]
    x2 = [0, 1, 0]
    label = 1
    margin = 0.0
    print(cosine_embedding_loss(x1, x2, label, margin))