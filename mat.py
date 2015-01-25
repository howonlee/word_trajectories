from nltk.corpus import brown
import numpy as np
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def get_bigrams(ls):
    return zip(ls, ls[1:])

def plot_sparse(mat):
    plt.cla()
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

def bigram_to_address(bigram, word_map):
    addresses = []
    for prevword, word in bigram:
        addresses.append((word_map[prevword], word_map[word]))
    return addresses

if __name__ == "__main__":
    bigrams = get_bigrams(brown.words())
    word_dict = word_mapping(brown.words())
    addresses = bigram_to_address(bigrams, word_dict)
    curr_mat = sci_sp.dok_matrix((len(word_dict), len(word_dict)))
    frame_count = 0
    bigram_range = 400
    for address_idx in xrange(bigram_range):
        address = addresses[address_idx]
        frame_count += 1
        curr_mat[address[0], address[1]] += 1
        fname = "_tmp%09d.png" % frame_count
        print fname
        plt.clf()
        mat = curr_mat[:bigram_range//2, :bigram_range//2].todense()
        np.fill_diagonal(mat, 0)
        plt.spy(mat)
        plt.xlabel("start word label")
        plt.ylabel("end word label")
        plt.savefig(fname)
