# Given a binary tree and value, find if there is a node with this value in a
# depthFirstSearch and BreadthFirstSearch.

# Tree:
#          3
#     5        1
#   6   2    0   8
#     7   4



class TreeNode():
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root0 = TreeNode(0, None, None)         
root8 = TreeNode(8, None, None)
root1 = TreeNode(1, root0, root8)
root4 = TreeNode(4, None, None)
root7 = TreeNode(7, None, None)
root2 = TreeNode(2, root7, root4) 
root6 = TreeNode(6, None, None)
root5 = TreeNode(5, root6, root2)
root3 = TreeNode(3, root5, root1)


print(oneDepthNodes(root3, 3))    


def depthFirstSearch(tree, value):
    if tree == None:
        return False
    elif tree.val == value:
        return True
    elif tree.val != value and tree.left == None and tree.right == None:
        return False
    elif tree.val != value and tree.left == None:
        return depthFirstSearch(tree.right, value)
    elif tree.val != value and tree.right == None:
        return depthFirstSearch(tree.left, value)
    else:
        return depthFirstSearch(tree.left, value) or depthFirstSearch(tree.right, value)

print(depthFirstSearch(root3, 8))
print(depthFirstSearch(root3, 5))
print(depthFirstSearch(root3, 7))
print(depthFirstSearch(root3, 9))



