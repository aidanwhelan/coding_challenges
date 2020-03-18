# serialize_binary.py
#
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
#
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string.
#
# For example, given the following Node class
#
#         class Node:
#             def __init__(self, val, left=None, right=None):
#                 self.val = val
#                 self.left = left
#                 self.right = right
# Mar 8 2020
# Aidan Whelan

class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(node.val)
node.left

#serialize function returns string
#serialize function takes root node
# NOTE: DEPTH FIRST
result = ''

def serialize(node):
    global result
    if(node.left):
        print(node.left.val)
        result += str(node.left.val+'/')
        serialize(node.left)
    else:
        print('-/')
        result += ('-/')
    if(node.right):
        print(node.right.val)
        result += str(node.right.val+'/')
        serialize(node.right)
    else:
        print('-/')
        result += ('-/')

serialize(node)
# left
# left.left
# NO LEFT/
# NO RIGHT/
# NO RIGHT/
# right
# NO LEFT/
# NO RIGHT/
print(result)
