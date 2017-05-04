from Insertion_sort import insertion_sort


def bucket_sort(A):
    n = len(A)
    L = [[] for i in range(n)]
    B = []
    for i in A:
        j = int(n * i)
        L[j].append(i)
    for k in L:
        insertion_sort(k)
    for lis in L:
        for liss in lis:
            B.append(liss)
    return B


if __name__ == '__main__':
    A = [.78, .17, .39, .26, .72, .94, .21, .12, .23, .68]
    print(bucket_sort(A))