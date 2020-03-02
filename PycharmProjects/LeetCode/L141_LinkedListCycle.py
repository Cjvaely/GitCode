# 给定一个链表，判断链表中是否有环。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#
#
#  示例 1：
#
#  输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
#  示例 2：
#
#  输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
#  示例 3：
#
#  输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
#
#
#
#
#
#  进阶：
#
#  你能用 O(1)（即，常量）内存解决此问题吗？
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        """
        :param head: : ListNode
        :return: bool
        解法：
        1. 暴力法：遍历列表，hash/set，空间复杂度O(n)
        2. 快慢指针 （环形列表的套路）,空间复杂度O(1)
        """
        """
        快慢指针：设置两个指针，快指针跳两步，慢指针跳一步
        有环：快慢指针会相遇
        无环：快指针会遍历到空
        时间复杂度O(n)
        空间复杂度O(1)
        """
        if (head == None) or (head.next == None):
            return False
        # 设置快慢指针
        slow, fast = head, head.next
        # 只要两个指针不相等
        while slow != fast:
            # 判断fast是否为空，或下一指针是否为空（防止跳过空指针）
            if fast == None or fast.next == None:
                return False
            else:
                # 更新快慢指针
                slow = slow.next
                fast = fast.next.next
        # while end: 两个指针相等
        return True


# leetcode submit region end(Prohibit modification and deletion)
