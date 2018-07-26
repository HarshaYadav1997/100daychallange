class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


def maxHeight(root):
    if root is None:
        return 0
    else:
        leftH = maxHeight(root.left)
        rightH = maxHeight(root.right)
        if leftH > rightH:
            return leftH + 1
        else:
            return rightH + 1


# tree  value insertion
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print("Tree In-order traversal : ")
printInorder(root)
print("Height of tree is %d" % (maxHeight(root)))
