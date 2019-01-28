# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]

# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

def reconstruct(preorder, inorder):
    if not preorder and not inorder:
        return None
    if len(preorder) == len(inorder) == 1:
        return preorder[0]

    root = preorder[0]
    root_i = inorder.index(root)
    root.left = reconstruct(preorder[1:1 + root_i], inorder[0:root_i])
    root.right = reconstruct(preorder[1 + root_i:], inorder[root_i + 1:])
    return root