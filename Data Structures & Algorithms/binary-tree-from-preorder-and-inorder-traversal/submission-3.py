# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pos = {val: i for i, val in enumerate(inorder)}
        idx = 0

        def solve(start, end):
            nonlocal idx

            if start > end:
                return None

            root_val = preorder[idx]
            idx += 1

            root = TreeNode(root_val)

            mid = pos[root_val]

            root.left = solve(start, mid - 1)
            root.right = solve(mid + 1, end)

            return root

        return solve(0, len(inorder) - 1)