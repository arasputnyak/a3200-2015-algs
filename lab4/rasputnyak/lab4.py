from sys import stdin
elem = [int(i) for i in stdin.readline().split()]
k = 10
def insertionsort(lst):
    c = 0
    for j in range(1, len(lst)):
        i = j - 1
        while i > -1 and lst[i] > lst[j]:
            swap(lst, i, j)
            c += 1
    if c > 0:
        insertionsort(lst)
    return lst
def swap(lst, i, j):
    x = lst[i]
    lst[i] = lst[j]
    lst[j] = x
def mergesort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result
def sortirovka(lst):
    if len(lst) < k:
        return insertionsort(lst)
    else:
        return mergesort(lst)
print(sortirovka(elem))