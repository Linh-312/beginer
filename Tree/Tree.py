class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inPrint(node):
    if node is not None:
        inPrint(node.left)
        print(node.key)
        inPrint(node.right)


# chèn thêm node mới
def insert(node, key):
    if node is None:
        return Node(key)
    elif key > node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


# tìm chiều cao nhỏ nhất của cây
def treeMin(node):
    if node is not None:
        return min(treeMin(node.left), treeMin(node.right)) + 1
    return -1


def diameter(node):
    node_left = treeMax(searchHigh(node, node.left.key))
    node_right = treeMax(searchHigh(node, node.right.key))
    print (node.right.key,node.left.key)
    print (node_right,node_left)
    return node_right + node_left + 2


# tìm chiều cao lớn nhất của cây
def treeMax(node):
    if node is not None:
        return max(treeMax(node.left), treeMax(node.right)) + 1
    return -1


def searchHigh(node, data):
    if node is not None:
        if node.key == data:
            return node
        elif node.key > data:
            return searchHigh(node.right, data)
        else:
            return searchHigh(node.left, data)
    return None


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 10)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 90)

inPrint(root)
print(treeMax(root))
print(diameter(root))