from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List to hold children nodes

    def add_child(self, child_node):
        self.children.append(child_node)

def bfs(root):
    if root is None:
        return []

    queue = deque([root])  # Initialize the queue with the root node
    result = []  # List to store the order of visited nodes

    while queue:
        current_node = queue.popleft()  # Dequeue the front node
        result.append(current_node.value)  # Visit the current node

        # Enqueue all children of the current node
        for child in current_node.children:
            queue.append(child)

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

    # Perform BFS
    bfs_result = bfs(root)

    # Print the BFS result
    print("BFS Traversal Order:", bfs_result)