# ---------Problem---------------
# This problem was asked by Dropbox.

# Given the root to a binary search tree, find the second largest node in the tree.

# ------------------Solution----------------
# An in-order traversal of the binary search tree would give us all the nodes of the tree in sorted order. So the naive solution here might be do an in-order traversal of the tree, store it in an array, and return the second-to-last element in the array.

# This takes O(N) time and space since we have to go through and store every node in the tree.

def second_largest(root):
    def inorder(node):
        if not node or count[0] == 2:
            return

        if node.right:
            inorder(node.right)

        count[0] += 1
        if count[0] == 2:
            val.append(node.val)
            return

        if node.left:
            inorder(node.left)

    count = [0]
    val = []
    inorder(root)
    return val[0]