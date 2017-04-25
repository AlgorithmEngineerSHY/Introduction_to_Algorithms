import random
import math
a = [x for x in range(10)]
random.shuffle(a)
print(a)

def merge_sort(a, l, r):
    if l < r:
        mid = int((l + r) / 2)
        merge_sort(a, l, mid)
        merge_sort(a, mid + 1, r)
        merge(a, l, mid, r)

def merge(a, l, mid, r):
    L = a[l: mid + 1].copy()
    L.append(math.inf)
    R = a[mid + 1: r + 1].copy()
    R.append(math.inf)
    i = j = 0
    for k in range(l, r + 1):
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
merge_sort(a, 0, 9)
print(a)




