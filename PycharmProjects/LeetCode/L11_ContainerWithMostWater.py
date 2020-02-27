# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
#  说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
#  示例:
#
#  输入: [1,8,6,2,5,4,8,3,7]
#  输出: 49
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height):
        """
        :param height: : List[int]
        :return: maxArea
        :exception:
        要矩阵面积最大化，两条垂直线的距离越远越好，两条垂直线的最短长度也要越长越好。
        我们设置两个指针 left 和 right，分别指向数组的最左端和最右端。
        此时，两条垂直线的距离是最远的，若要下一个矩阵面积比当前面积来得大，
        必须要把 height[left] 和 height[right] 中较短的垂直线往中间移动，
        看看是否可以找到更长的垂直线。
        参考：https://leetcode-cn.com/problems/container-with-most-water/solution/shuang-zhi-zhen-jie-fa-by-jalan/
        时间复杂度：O(n)O(n)，一次扫描。
        空间复杂度：O(1)O(1)，使用恒定的空间。
        """
        max_area = 0    # 最大面积
        l = 0   # 左指针
        r = len(height) - 1   # 右指针

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = area if area > max_area else max_area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


# leetcode submit region end(Prohibit modification and deletion)
