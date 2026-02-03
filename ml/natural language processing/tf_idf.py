'''
TF-IDF Vectorizer.
'''

import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    if not documents or all(doc.strip() == "" for doc in documents):
        return np.array([]), []
    
    tokenized = [doc.lower().split() for doc in documents]
    
    all_tokens = set()
    for doc in tokenized:
        all_tokens.update(doc)
    
    vocab = sorted(all_tokens)
    
    word_to_idx = dict()
    for idx, word in enumerate(vocab):
        word_to_idx[word] = idx
    
    n_docs = len(documents)
    n_vocab = len(vocab)
    
    if n_vocab == 0 or n_docs == 0:
        return np.array([]), []
    
    df = Counter()
    for doc in tokenized:
        unique_terms = set(doc)
        for term in unique_terms:
            df[term] += 1
            
    idf = {}
    for word in vocab:
        idf[word] = math.log(n_docs / df[word])
    
    tfidf_matrix = np.zeros((n_docs, n_vocab), dtype=float)
    
    for doc_idx, doc in enumerate(tokenized):
        doc_len = len(doc)
        if doc_len == 0:
            continue
        
        term_counts = Counter(doc)
        for word, count in term_counts.items():
            if word in word_to_idx:
                w_idx = word_to_idx[word]
                tf = count / doc_len
                tfidf_matrix[doc_idx, w_idx] = tf * idf[word]
                
    return tfidf_matrix, vocab


if __name__ == "__main__":
    documents = ["the cat sat", "the dog ran"]
    matrix, vocab = tfidf_vectorizer(documents)
    print(f"{matrix.shape}, {vocab}")