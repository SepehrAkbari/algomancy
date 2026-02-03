'''
TF-IDF Vectorizer.

Implement a TF-IDF vectorizer that converts text documents into numerical feature vectors. Return both the TF-IDF matrix and the vocabulary.

Examples

Input: documents=["the cat sat", "the dog ran"]
Output: matrix shape (2, 5), vocab=["cat", "dog", "ran", "sat", "the"]
Input: documents=["hello world", "world hello hello"]
Output: matrix shape (2, 2), vocab=["hello", "world"]

💡 Hint 1
Use str.split() and str.lower() for tokenization. Use set() to build vocabulary and sorted() for consistent ordering.
💡 Hint 2
Use Counter for term frequencies and document frequency counting. Use math.log() for IDF calculation.
💡 Hint 3
Use np.zeros() to initialize the matrix. Create a word-to-index mapping with enumerate() for efficient matrix filling.

Requirements

Return tuple: (tfidf_matrix, vocabulary)
tfidf_matrix: np.ndarray of shape (n_docs, n_vocab)
vocabulary: list[str] of unique terms, sorted alphabetically
Tokenize by splitting on whitespace and converting to lowercase
Handle empty documents and empty corpus gracefully
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