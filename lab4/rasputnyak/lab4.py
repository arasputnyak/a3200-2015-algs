from sys import stdin
elem = [int(i) for i in stdin.readline().split()]
k = 10

def insertion_sort(lst):
   for i in range(len(lst)):
       key = lst[i]
       j = i
       while j > 0 and lst[j - 1] > key:
           lst[j] = lst[j - 1]
           j -= 1
       lst[j] = key
   return lst

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
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

def sort(lst):
    if len(lst) < k:
        return insertion_sort(lst)
    else:
        return merge_sort(lst)

print(sort(elem))
