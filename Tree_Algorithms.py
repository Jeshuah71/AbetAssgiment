from Algo_and_Struts_06_i_tree_node import TreeNode

def numberOfLeaves(n :TreeNode) -> int:
    if n is None:
        return 0  # This will be considered the base case when node is none and it has no leaves
    if n.is_leaf():
        return 1  # A leaf node that contributes 1 to the count
    
    # This is where the recursive case occurs: count leaves in left and right subtrees
    return numberOfLeaves(n.left_child) + numberOfLeaves(n.right_child)
	
def numberOfNodesWithASingleChild(n: TreeNode) -> int:
    if n is None:
        return 0  # Base case: If the node is None, return 0
    
    count = 0
    # Check if the node has exactly one child
    if (n.left_child is not None and n.right_child is None) or \
       (n.left_child is None and n.right_child is not None):
        count = 1 

    # Recursive case: Check left and right subtrees
    return count + numberOfNodesWithASingleChild(n.left_child) + numberOfNodesWithASingleChild(n.right_child)
    
def numberOfNodesWithTwoChildren(n :TreeNode)  -> int:
    if n is None:
        return 0 # This is the base case where the node is none and it has no children.
    
    count = 0
    # Checking if the node has to children
    if n.left_child is not None and n.right_child is not None:
        count = 1 # increment the count if the node has two children
    
    # Applying recursive case: Check the left and right subtrees
    return count + numberOfNodesWithTwoChildren(n.left_child) + numberOfNodesWithTwoChildren(n.right_child)
	
def numberOfNodesWithEvenDataItems(n :TreeNode)  -> int:
    if n is None:
        return 0 # Base case where the node is none and it has no data
    
    count = 0 
    # Check if the node's value is even
    if n.value % 2 == 0:
        count = 1 # Increment the count if the node's value is even
    
    #Recursive case: Checking left and right subtrees
    return count + numberOfNodesWithEvenDataItems(n.left_child) + numberOfNodesWithEvenDataItems(n.right_child)
def sumOfAllItems(n: TreeNode) -> int:
    if n is None:
        return 0  # Base case where the node is None, it contributes 0 to the sum.

    # Recursive case: Sum the current node's value and the values of left and right subtrees.
    return n.value + sumOfAllItems(n.left_child) + sumOfAllItems(n.right_child)
def printRuntimes():
    # Since these algorithms traverse the entire tree, they are O(n).
    print("BigOh runtime of numberOfLeaves is: O(n)")
    print("BigOh runtime of numberOfNodesWithOneNonNullChild is: O(n)")
    print("BigOh runtime of numberOfNodesWithTwoNonNullChildren is: O(n)")
    print("BigOh runtime of numberOfNodesWithEvenDataItems is: O(n)")
    print("BigOh runtime of sumOfAllItems is: O(n)")

def main():
    # Creating a test tree
    root = TreeNode(10, 10)
    root.left_child = TreeNode(5, 5)
    root.right_child = TreeNode(15, 15)
    root.left_child.left_child = TreeNode(3, 3)
    root.left_child.right_child = TreeNode(7, 7)
    root.right_child.right_child = TreeNode(20, 20)

    # Running the methods and print their results
    print("Number of leaves:", numberOfLeaves(root))
    print("Number of nodes with a single child:", numberOfNodesWithASingleChild(root))  
    print("Number of nodes with two children:", numberOfNodesWithTwoChildren(root)) 
    print("Number of nodes with even data items:", numberOfNodesWithEvenDataItems(root)) 
    print("Sum of all items:", sumOfAllItems(root)) 

    # Printing the Big-O runtimes
    printRuntimes()

if __name__ == "__main__":
    main()

		