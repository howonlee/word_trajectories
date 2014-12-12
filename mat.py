from nltk.corpus import brown
import numpy as np
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def get_bigrams(ls):
    return zip(ls, ls[1:])

def plot_sparse(mat):
    plt.spy(mat, markersize=0.1)
    plt.xlabel("start word label")
    plt.ylabel("end word label")
    plt.show()

def word_mapping(words):
    curr_count = 0
    state_map = {}
    for word in words:
        if word not in state_map:
            state_map[word] = curr_count
            curr_count += 1
    return state_map

def bigram_to_mat(bigram, word_map):
    mat = sci_sp.dok_matrix((len(word_map), len(word_map)))
    for prevword, word in bigram:
        mat[word_map[prevword], word_map[word]] += 1
    return mat

if __name__ == "__main__":
    bigrams = get_bigrams(brown.words())
    word_dict = word_mapping(brown.words())
    mat = bigram_to_mat(bigrams, word_dict)
    mat = mat[:1000, :1000]
    plot_sparse(mat)
