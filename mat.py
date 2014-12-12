from nltk.corpus import brown

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

print find_ngrams(brown.words(), 2)
