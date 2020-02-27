# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
#  示例:
#
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#  说明:
#
#
#  必须在原数组上操作，不能拷贝额外的数组。
#  尽量减少操作次数。
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 解法：采用两次遍历法。
    def moveZeroes(self, nums):
        """
        :param nums: : List[int]
        :return: Do not return anything, modify nums in-place instead.
        """
        j = 0
        # 第一次遍历列表
        for i in range(len(nums)):
            # 如果当前不是0，则j+1计数
            if nums[i] != 0:
                # 把所有不是0的数放到列表前面
                nums[j] = nums[i]
                # j计数+1
                j += 1
        # 再次遍历，将为0的地方填上0
        for i in range(j, len(nums)):
            nums[i] = 0

    # 一次遍历法
    def moveZeroesOneCircle(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
# leetcode submit region end(Prohibit modification and deletion)

