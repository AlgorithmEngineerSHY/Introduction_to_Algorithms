import random
a = [x for x in range(10)]
random.shuffle(a)
print(a)

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        while key < a[i - 1] and i >= 1:
            a[i] = a[i - 1]
            i -= 1
        a[i] = key

insertion_sort(a)
print(a)
