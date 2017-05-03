def parent(i):
    return int((i - 1) / 2)

def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def max_heapify(A, i):
    l = left(i)
    r = right(i)
    n = len(A) - 1
    if l <= n and A[i] < A[l]:
        largest = l
    else:
        largest = i
    if r <= n and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    n = len(A)
    for i in range(int(n / 2), -1, -1):
        max_heapify(A, i)


def heap_sort(A):
    build_max_heap(A)
    L_sort = []
    n = len(A) - 1
    for i in range(n, 0, -1):
        L_sort.append(A[0])
        A[0], A[i] = A[i], A[0]
        del A[i]
        max_heapify(A, 0)
    L_sort.append(A[0])
    print(L_sort)

if __name__ == '__main__':
    heap_sort([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])



