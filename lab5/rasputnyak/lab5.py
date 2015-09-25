import random
from sys import stdin
elem = [int(i) for i in stdin.readline().split()]
def quicksort(lst, frst, last):
    if frst < last:
        mid = randompartition(lst, frst, last)
        quicksort(lst, frst, mid - 1)
        quicksort(lst, mid + 1, last)
def partition(lst, frst, last):
    x = lst[last]
    i = frst - 1
    for j in range(frst, last):
        if lst[j] <= x:
            i += 1
            swap(lst, i, j)
    swap(lst, i + 1, last)
    return i + 1
def randompartition(lst, frst, last):
    i = random.randint(frst, last)
    swap(lst, last, i)
    return partition(lst, frst, last)
def swap(lst, i, j):
    x = lst[i]
    lst[i] = lst[j]
    lst[j] = x
quicksort(elem, 0, len(elem) - 1)
print(elem)

