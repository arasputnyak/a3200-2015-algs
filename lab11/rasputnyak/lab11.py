from sys import stdin
from sys import stdout

def area(lst):
    ar = 0
    max_ar = 0
    if len(lst) <= 1:
        return ar
    else:
        max = lst[0]
        for i in range(1, len(lst)):
            if lst[i] >= max:
                if ar > max_ar:
                    max_ar = ar
                ar = 0
                max = lst[i]
            else:
                    ar += max - lst[i]
    return max_ar

if __name__ == '__main__':
    elem = [int(i) for i in stdin.readline().split()]
    stdout.write(str(area(elem)))
