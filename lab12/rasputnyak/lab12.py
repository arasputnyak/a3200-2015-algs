class Set:
    def add(self, value):
        pass

    def iterate(self):
        pass

class Node:
    def __init__(self):
        self.data   = None
        self.parent = None
        self.left   = None
        self.right  = None

class UnbalancedBinarySearchTree(Set):
    def __init__(self):
        self.head = Node()

    def newNode(self, data):
        node = Node()
        node.data = data
        return node

    def add(self, value):
        nodeValue = self.newNode(value)
        y = None
        x = self.head
        while x.data != None:
            y = x
            if nodeValue.data < x.data:
                x = x.left
                if x == None:
                    break
            else:
                x = x.right
                if x == None:
                    break
        nodeValue.parent = y
        if y == None:
            self.head = nodeValue
        else:
            if nodeValue.data < y.data:
                y.left = nodeValue
            else:
                y.right = nodeValue

    def contains(self, value):
        y = self.head
        if y == None:
            print("false")
        else:
            if value == y.data:
                print("true")
            if value < y.data:
                x = y.left
                newTree = UnbalancedBinarySearchTree()
                newTree.head = x
                newTree.contains(value)
            if value > y.data:
                x = y.right
                newTree = UnbalancedBinarySearchTree()
                newTree.head = x
                newTree.contains(value)

    def tree_min(self, x):
        node = self.newNode(x)
        while node.left != None:
            node = node.left
        return node.data

    def tree_walk(self):
        x = self.head
        if x != None:
            print(x.data)
            y = x.left
            z = x.right
            newTree1 = UnbalancedBinarySearchTree()
            newTree1.head = y
            newTree2 = UnbalancedBinarySearchTree()
            newTree2.head = z
            newTree1.tree_walk()
            newTree2.tree_walk()

    def tree_successor(self, x):
        if x.right != None:
            return self.tree_min(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y


    def iterate(self):
        for i in range(0, len(self.values)):
            yield self.values[i]

    def __iter__(self):
        # approach with yield, can be inlined into this method too, extracted for example purposes
        return self.iterate()
        # manual approach with next() and StopIteration(). Isn't preferred
        # return TreeGeneratorManual(self)
        # we can also just use the generator from list in this example
        # return self.values.__iter__()



tree = UnbalancedBinarySearchTree()
tree.add(3)
tree.add(6)
tree.add(2)
tree.add(12)
tree.add(4)
tree.add(1)
tree.contains(7)
tree.contains(8)
print(tree.tree_min(3))
#tree.tree_walk()




