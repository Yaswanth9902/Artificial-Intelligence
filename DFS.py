class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List to hold children nodes

    def add_child(self, child_node):
        self.children.append(child_node)

def dfs(root):
    result = []  # List to store the order of visited nodes
    stack = [root]  # Initialize the stack with the root node

    while stack:
        current_node = stack.pop()  # Pop the top node from the stack
        result.append(current_node.value)  # Visit the current node

        # Push all children of the current node onto the stack
        for child in reversed(current_node.children):  # Reverse to maintain order
            stack.append(child)

    return result

# Example usage
if __name__ == "__main__":
    # Create the tree structure
    root = TreeNode(1)
    child_a = TreeNode(2)
    child_b = TreeNode(3)
    child_c = TreeNode(4)
    child_d = TreeNode(5)

    # Build the tree
    root.add_child(child_a)
    root.add_child(child_b)
    child_a.add_child(child_c)
    child_a.add_child(child_d)

    # Perform DFS
    dfs_result = dfs(root)

    # Print the DFS result
    print("DFS Traversal Order:", dfs_result)