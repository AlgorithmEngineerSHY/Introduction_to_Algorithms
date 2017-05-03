from Heap_sort import *
import numpy as np

def heap_maximum(A):
    return A[0]


def heap_extract_max(A):
    if len(A) == 1:
        return A[0]
    else:
        max = A[0]
        A[0] = A[len(A) - 1]
        del A[len(A) - 1]
        max_heapify(A, 0)
        return max


def heap_increase_key(A, i, key):
    if A[i] >= key:
        print('error')
        return
    else:
        A[i] = key
        while A[i] > A[parent(i)] and i != 0:
            A[i], A[parent(i)] = A[parent(i)], A[i]
            i = parent(i)

def max_heap_insert(A, key):
    A.append(-np.inf)
    heap_increase_key(A, len(A) - 1, key)


if __name__ == '__main__':
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_max_heap(A)
    print(A)
    print(heap_extract_max(A))
    print(heap_maximum(A))
    print(max_heap_insert(A, 13))
    print(A)