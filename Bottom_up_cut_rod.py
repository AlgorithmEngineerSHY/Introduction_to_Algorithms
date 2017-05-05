import numpy as np


def extended_bottom_up_cut_rod(p, n):
    A = [x for x in range(0, n + 1)]  #how to cut
    B = [x for x in range(0, n + 1)] #best price
    for i in range(1, n + 1):
        maxx = -np.inf
        for j in range(1, i + 1):
            if maxx < max(maxx, p[j - 1] + B[i - j]):
                maxx = max(maxx, p[j - 1] + B[i - j])
                A[i] = j
        B[i] = maxx
    return A, B


def print_cut_rod_solution(p, n):
    A, B = extended_bottom_up_cut_rod(p, n)
    print('best price is: {}'.format(B[n]))

    while n > 0:
        print(A[n])
        n -= A[n]


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print_cut_rod_solution(p, 7)
    #print(extended_bottom_up_cut_rod(p, 10))
