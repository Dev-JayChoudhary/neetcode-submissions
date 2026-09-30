# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        def solve(root):
            nonlocal maxSum
            if root is None:
                return 0
            
            l = solve(root.left)
            r = solve(root.right)

            koi_ek_acha = max(l, r) + root.val
            sirf_root_acha = root.val
            neeche_hi_answer = l + r +root.val

            maxSum = max(maxSum, koi_ek_acha, sirf_root_acha, neeche_hi_answer)

            return max(koi_ek_acha, sirf_root_acha)

        solve(root)
        return maxSum