class Node:
    def __init__(self, num, leftNode, rightNode):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.num = num

    def add(self, node):
        if node.num >= self.num:
            if self.rightNode is None:
                self.rightNode = node
            else:
                self.rightNode.add(node)
        elif node.num < self.num:
            if self.leftNode is None:
                self.leftNode = node
            else:
                self.leftNode.add(node)

    def print(self):
        if self.leftNode is not None:
            self.leftNode.print()
        
        print(self.num)

        if self.rightNode is not None:
            self.rightNode.print()

# Sets up the binary tree
root = Node(50, None, None)
root.add(Node(60, None, None))
root.add(Node(40, None, None))
root.add(Node(10, None, None))
root.add(Node(80, None, None))
root.add(Node(100, None, None))
root.add(Node(70, None, None))
root.add(Node(0, None, None))
root.add(Node(20, None, None))
root.add(Node(30, None, None))
root.add(Node(90, None, None))
root.print()