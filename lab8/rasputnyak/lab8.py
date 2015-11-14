class Queue:
    def pop(self):
        pass

    def push(self):
        pass

    def size(self):
        pass

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def size(self):
        return len(self._stack)

class StackQueue(Queue):
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def push(self, x):
        self.stack_1.push(x)
        print("ok")

    def pop(self):
        s = self.stack_1.size()
        if self.stack_2.size() == 0:
            if self.size() > 0:
                for i in range(s):
                    self.stack_2.push(self.stack_1.pop())
                q = self.stack_2.pop()
                print(q)
                return q
            else:
                print("empty")
                return None
        else:
            q = self.stack_2.pop()
            print(q)
            return q

    def size(self):
        return self.stack_1.size() + self.stack_2.size()

class MaxElementQueue(Queue):
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        self.max = None

    def push(self, x):
        if self.size() == 0:
            self.max = x
        else:
            if x >= self.max:
                self.max = x
        self.stack_1.push(x)
        print("ok")

    def pop(self):
        lst = []
        self.max = - (1000 ** 10)
        s = self.stack_1.size()
        if self.stack_2.size() == 0:
            if self.size() > 0:
                for i in range(1, s):
                    e = self.stack_1.pop()
                    self.stack_2.push(e)
                    if e > self.max:
                        self.max = e
                q = self.stack_1.pop()
                print(q)
                return q
            else:
                print("empty")
                return None
        else:
            q = self.stack_2.pop()
            print(q)
            s = self.stack_2.size()
            for i in range(s):
                e = self.stack_2.pop()
                if e > self.max:
                    self.max = e
                lst.append(e)
            lst.reverse()
            for i in range(len(lst)):
                self.stack_2.push(lst[i])
            return q

    def size(self):
        return self.stack_1.size() + self.stack_2.size()

    def max_elem(self):
        if self.size() == 0:
            print("empty")
        else:
            print(self.max)
            return self.max





