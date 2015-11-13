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
        a = len(self._stack) - 1
        k = self._stack[a]
        del self._stack[a]
        return k

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
        if self.size() > 0:
            for i in range(s):
                self.stack_2.push(self.stack_1.pop())
            print(self.stack_2.pop())
        else:
            print("empty")

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
        s = self.stack_1.size()
        if self.size() > 0:
            for i in range(s):
                self.stack_2.push(self.stack_1.pop())
            print(self.stack_2.pop())
        else:
            print("empty")

    def size(self):
        return self.stack_1.size() + self.stack_2.size()

    def max_elem(self):
        if self.size() == 0:
            print("empty")
        else:
            print(self.max)





