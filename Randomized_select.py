from Quick_sort import randomized_partition
import random


def randomized_select(A, start, end, i):
    if start == end:
        return A[start]

    mid = randomized_partition(A, start, end)
    if mid == i:
        return A[i]
    if mid > i:
        return randomized_select(A, start, mid - 1, i)
    if mid < i:
        return randomized_select(A, mid + 1, end, i)

if __name__ == '__main__':
    A = [random.randint(0, 10) for i in range(10)]
    print(A)
    print(randomized_select(A, 0, 9, 3))
