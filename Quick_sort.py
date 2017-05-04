import random

def quick_sort(A, start, end):
    if start < end:
        mid = partition(A, start, end)
        quick_sort(A, start, mid - 1)
        quick_sort(A, mid + 1, end)


def partition(A, start, end):
    mid_num = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] < mid_num:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    i += 1
    return i

def randomized_partition(A, start, end):
    rand = random.randint(start, end)
    A[rand], A[end] = A[end], A[rand]
    return partition(A, start, end)


def randomized_quick_sort(A, start, end):
    if start < end:
        mid = randomized_partition(A, start, end)
        randomized_quick_sort(A, start, mid - 1)
        randomized_quick_sort(A, mid + 1, end)



if __name__ == '__main__':
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    randomized_quick_sort(A, 0, 9)
    print(A)
