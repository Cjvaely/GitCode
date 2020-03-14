# 给定一个二叉树，返回它的中序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        使用递归算法解决：
        左根右=》左-打印-右
        """
        # res = []
        #
        # def inTrave(root):
        #     if not root:
        #         return res
        #     inTrave(root.left)
        #     res.append(root.val)
        #     inTrave(root.right)
        # inTrave(root)
        # return res
        """
        使用栈遍历
        """
        res = []
        stack = []
        curr = root

        while curr or len(stack) != 0:
            # 如果当前结点非空
            while curr:
                # 将当前结点压入栈中
                stack.append(curr)
                # 转向左子树, 1. 左
                curr = curr.left
            # 此时遍历到树的最左结点，出栈
            curr = stack.pop()
            # 访问当前结点值， 2. 根
            res.append(curr.val)
            # 访问右结点 3. 右
            curr = curr.right

        return res






# leetcode submit region end(Prohibit modification and deletion)
