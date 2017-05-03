import numpy as np

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -np.inf
    sum = 0
    left_max_i = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum >= left_sum:
            left_sum = sum
            left_max_i = i
    right_sum = -np.inf
    sum = 0
    right_max_i = 0
    for i in range(mid + 1, high + 1, 1):
        sum += A[i]
        if sum >= right_sum:
            right_sum = sum
            right_max_i = i
    return left_sum + right_sum, left_max_i, right_max_i



def find_maximum_subarray(A, low, high):
    if high == low:
        return A[low], low, high
    else:
        mid = int((low + high) / 2)
        left_max, left_low, left_high = find_maximum_subarray(A, low, mid)
        right_max, right_low, right_high = find_maximum_subarray(A, mid + 1, high)
        cross_max, cross_low, cross_high = find_max_crossing_subarray(A, low, mid, high)
    if left_max >= left_max and left_max >= cross_max:
        return left_max, left_low, left_high
    elif right_max >= left_max and right_max >= cross_max:
        return right_max, right_low, right_high
    else:
        return cross_max, cross_low, cross_high

if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_maximum_subarray(A, 0, 15))