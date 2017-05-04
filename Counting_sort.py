
def counting_sort(A):
    n = len(A)
    B = [0 for i in range(n)]
    k = max(A)
    C = [0 for i in range(k + 1)]
    for i in A:
        C[i] += 1
    for i in range(k):
        C[i + 1] += C[i]
    for i in A:
        B[C[i] - 1] = i
        C[i] -= 1
    return B



if __name__ == '__main__':
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    print(counting_sort(A))
