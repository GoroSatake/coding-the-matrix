from vec import Vec

def list2vec(L):
    return Vec(set(range(len(L))), {i:L[i] for i in range(len(L)) if L[i] != 0})
##    return Vec(set(range(len(L))), {i:L[i] for i in range(len(L))})
##L = [0, 1, 4, 9, 16]
##print(list2vec(L))

def zero_vec(D):
    return Vec(D, {})
