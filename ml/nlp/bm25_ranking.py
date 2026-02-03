'''
BM25 Ranking Score.
'''

import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    N = len(docs)
    if N == 0:
        return np.array([], dtype=float)
    
    dl = np.array([len(d) for d in docs])
    dl_avg = np.mean(dl)
    
    doc_tfs = [Counter(d) for d in docs]
    
    all_terms = set(query_tokens)
    
    df = {}
    for term in all_terms:
        df[term] = sum(1 for tf_map in doc_tfs if term in tf_map)
    
    idf = {}
    for term in all_terms:
        if df[term] > 0:
            idf[term] = math.log((N - df[term] + 0.5) / (df[term] + 0.5) + 1.0)
        else:
            idf[term] = 0.0
        
    scores = np.zeros(N, dtype=float)
    unique_qt = list(dict.fromkeys(query_tokens))
    
    for term in unique_qt:
        if idf[term] == 0:
            continue
        
        tfs = np.array([tf_map.get(term, 0) for tf_map in doc_tfs])
        
        scores += idf[term] * ((tfs * (k1 + 1)) / (tfs + k1 * (1 - b + b * (dl / dl_avg))))
        
    return scores

if __name__ == "__main__":
    query=["machine","learning"]
    docs=[["introduction","to","machine","learning"], 
          ["deep","learning","basics"], 
          ["cooking","pasta","guide"]]
    
    print(bm25_score(query, docs))