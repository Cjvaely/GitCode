# 给定一个二叉树，返回它的 前序 遍历。
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
# 输出: [1,2,3]
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归法：根-左-右
        :param root:
        :return:
        """
        # res = []
        #
        # def preTrave(root):
        #     if not root:
        #         return res
        #     res.append(root.val)
        #     preTrave(root.left)
        #     preTrave(root.right)
        #
        # preTrave(root)
        # return res

        """
        使用栈遍历  访问根结点 访问左  访问右
        """
        # 判空，防止出现NoneType
        if not root:
            return []

        res, stack = [], [root]

        # 栈非空
        while stack:
            curr = stack.pop()
            # 访问当前结点    1.根
            res.append(curr.val)
            # 右结点入栈，先进后出
            if curr.right: stack.append(curr.right)
            # 左结点入栈
            if curr.left: stack.append(curr.left)
        return res

# leetcode submit region end(Prohibit modification and deletion)
