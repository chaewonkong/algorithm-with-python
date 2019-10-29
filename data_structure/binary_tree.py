""" Binary Tree
"""

class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.v = v

l = Node(2)
l.left = Node(4)
l.right = Node(5)
r = Node(3)
r.left = Node(6)
r.right = Node(7)
root = Node(1)
root.left = l
root.right = r

PRE_ORDER = "pre-order"
IN_ORDER = "in-order"
POST_ORDER = "post-order"

def traverse(root, order):
    if root is None:
        return
    if order == "pre-order":
        print(root.v)
        traverse(root.left, order)
        traverse(root.right, order)
    if order == "in-order":
        traverse(root.left, order)
        print(root.v)
        traverse(root.right, order)
    if order == "post-order":
        traverse(root.left, order)
        traverse(root.right, order)
        print(root.v)

traverse(root, POST_ORDER)