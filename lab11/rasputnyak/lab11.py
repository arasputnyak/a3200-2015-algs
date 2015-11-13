from sys import stdin
from sys import stdout

def area(lst):
    lst2 = []
    s = 0
    if len(lst) <= 1:
        return s
    else:
        max = lst[0]
        Maxlst = maximum(lst)
        for i in range(1, len(lst) - 1):
            if lst[i] < max:
                s = s + (max - lst[i])
            else:
                if lst[i] < Maxlst:
                    max = lst[i]
                else:
                    max = lst[i + 1]
                lst2.append(s)
                s = 0
    return maximum(lst2)

def maximum(lst):
    max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] >= max:
            max = lst[i]
    return max

if __name__ == '__main__':
    elem = [int(i) for i in stdin.readline().split()]
    stdout.write(str(area(elem)))
