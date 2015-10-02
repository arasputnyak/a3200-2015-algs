from sys import stdin
lst = [int(i) for i in stdin.readline().split()]

def maximum(lst):
    maxx = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > maxx:
            maxx = lst[i]
    return maxx

def number(n):
    i = 0
    while n > 0:
        n = n // 10
        i = i + 1
    return i

def last_num(n, i):
    x = n // 10 ** i % 10
    return x

def radix_sort(lst):
    d = number(maximum(lst))
    for i in range(0, d):
        lst = counting_sort(lst, i)
    return lst

def counting_sort(lst, ind):
    k = 10
    lst2 = [0 for i in range(len(lst))]
    lst3 = [0 for i in range(k)]
    for j in range(len(lst)):
        lst3[last_num(lst[j], ind)] += 1
    for i in range(1, k):
        lst3[i] += lst3[i - 1]
    j = len(lst) - 1
    while (j >= 0):
        lst3[last_num(lst[j], ind)] -= 1
        lst2[lst3[last_num(lst[j], ind)]] = lst[j]
        j -= 1
    return lst2

print(radix_sort(lst))
