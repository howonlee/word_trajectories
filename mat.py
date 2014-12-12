from nltk.corpus import brown
import numpy as np
import scipy.sparse as sci_sp

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def ngram_iter(input_list, n):
    some yielding business

if __name__ == "__main__":
    create the sparse matrix
    but temporally...
