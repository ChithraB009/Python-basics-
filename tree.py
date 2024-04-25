
  root = TreeNode(2)
 obj2 = TreeNode(7)
 obj3 = TreeNode(5)
 obj4 = TreeNode(2)
 obj5 = TreeNode(6)
 obj6 = TreeNode(9)
 obj7 = TreeNode(5)
 obj8 = TreeNode(11)
 obj9 = TreeNode(4)

 root.left = obj2
 root.right = obj3
 obj2.left = obj4
 obj2.right = obj5
 obj3.left = obj6
 obj3.right = obj7
 obj4.left = obj8
 obj4.right = obj9

# Trees   
 
 
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
 
def printPreOrder(root):
    if root == None:
        return
 
    # root, left_subtree, right_subtree 
    print(root.data, end = " ")
    printPreOrder(root.left)
    printPreOrder(root.right)
 
def printInOrder(root):
    if root == None:
        return
 
    # left_subtree, root, right_subtree 
 
    printInOrder(root.left)
    print(root.data, end = " ")
    printInOrder(root.right) 
 
def printPostOrder(root):
    if root == None:
        return
 
    # left_subtree, right_subtree, root
 
    printPostOrder(root.left)
    printPostOrder(root.right) 
    print(root.data, end = " ")
 
# 1. objects creation (memory allocation) 
root = TreeNode(18)
# root:
# data = 15 
# left = None 
# right = None 
obj2 = TreeNode(15)
obj3 = TreeNode(20)
obj4 = TreeNode(25)
obj5 = TreeNode(30)
obj6 = TreeNode(45)
obj7 = TreeNode(80)
 
#    18 
#   15  20 
# 25 30 45 80
 
 
# 2- establishing links between nodes 
root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6 
obj3.right = obj7
printPostOrder(root)
