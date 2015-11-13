from sys import stdin
from sys import stdout

def triple(lst):
    lst2 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                s = lst[i] ** 2 + lst[j] ** 2
                lst2.append(s)
    lst3 = []
    for i in range(len(lst)):
        for j in range(len(lst2)):
            if lst[i] ** 2 == lst2[j]:
                lst3.append(lst[i])
    result = len(lst3) // 2
    return result

if __name__ == '__main__':
    elem = [int(i) for i in stdin.readline().split()]
    stdout.write(str(triple(elem)))

