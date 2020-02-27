# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#  注意：给定 n 是一个正整数。
#
#  示例 1：
#
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#  示例 2：
#
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
"""
思考方法：
1. 暴力解决？本题不可
2. 基本情况？
找最近重复子问题。
    1: 1
    2: 2
    3: 从第2级台阶上跨1步 / 从第1级跨2步  f(3) = f(1) + f(2)
    4: f(2) + f(3)
    f(n) = f(n-2) + f(n-1)
    与509斐波拉契数列问题解法一致。https://leetcode-cn.com/problems/fibonacci-number/
"""
class Solution:
    def climbStairs(self, n):
        """
        :param n: n-->int
        :return: count-->int
        f1 = 1
        f2 = 2
        f3 = f1 + f2
        f4 = f2 + f3
        fn = f(n-2) + f(n-1)
        """
        if n <= 2:
            return n
        # 只保存最后3个值，然后不断往前累加即可
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3

# leetcode submit region end(Prohibit modification and deletion)
