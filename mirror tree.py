"""
# 
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 
#  
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 
#  
# 
# Follow up: Solve it both recursively and iteratively.
# 
"""
def make_node(value, right = None, left = None):
    return {"value": value, "right": right, "left": left}
            
node7 = make_node(3, None, None)
node6 = make_node(4, None, None)
node5 = make_node(4, None, None)
node4 = make_node(3, None, None)
node3 = make_node(2, node6, node7)
node2 = make_node(2, node4, node5)
node1 = make_node(1, node2, node3)
#print("node1 is %s" % node1)

node8 = make_node(1, node6, node2)    
#print("node8 is %s" % node8)

node9 = make_node(2, None, node7)
node10 = make_node(1, node9, node9)

def compare(tree1, tree2):
    if tree1 == None and tree2 == None:
        return True
    elif tree1 == None and tree2 != None:
        return False
    elif tree1 != None and tree2 == None:
        return False
    elif tree1["value"] != tree2["value"]:
        return False
    elif tree1["value"] == tree2["value"]: 
        return compare(tree1["left"], tree2["right"]) and compare(tree1["right"], tree2["left"])
    
    
def simmetricTree(tree):
    if tree == None:
        return False
    elif tree["right"] == None and tree["left"] == None:
        return True
    elif tree["right"] == None and tree["left"] != None:
        return False
    elif tree["left"] == None and tree["right"] != None:
        return False
    elif tree["left"]["value"] != tree["right"]["value"]:
        return False
    else:# tree["left"]["value"] == tree["right"]["value"]:
        return compare(tree["left"]["left"], tree["right"]["right"]) and compare(tree["left"]["right"], tree["right"]["left"])
        
                
print(simmetricTree(node1))        
print(simmetricTree(node8))   
print(simmetricTree(node10)) 
