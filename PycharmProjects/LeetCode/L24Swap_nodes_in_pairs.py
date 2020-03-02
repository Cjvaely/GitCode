# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例:
#
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :param head: ListNode
        :return: ListNode
        1. 递归法
        时间复杂度：O(N)
        空间复杂度：O(N)
        """
        # # 但凡有空结点
        # if head is None or head.next is None:
        #     return head
        # else:
        #     # 交换结点
        #     first_node = head   # 1, 3
        #     second_node = head.next  # 2, 4
        #     # 第一轮：3->null       第二轮： 1->4
        #     first_node.next = self.swapPairs(second_node.next)
        #     # 第一轮：4->3,         第二轮：2->1
        #     second_node.next = first_node
        #     # 返回结果:4, 2(最终返回的结果)
        #     return second_node
        """
        2. 迭代法

        """
        # 新建一个空结点连接到head
        e_node = ListNode(-1)
        e_node.next = head
        prev_node = e_node

        while head and head.next:
            # first_node要交换的两个结点
            first_node = head  # 1，3
            second_node = head.next  # 2，4

            # 每次进入新一轮交换，prev_node就指向本次交换后的头（second_node）
            # 以确保上一轮交换的尾能与这一轮交换后的头相连
            prev_node.next = second_node  # -1->2 1->4

            # 交换两个结点
            first_node.next = second_node.next  # 1->3，3->null
            second_node.next = first_node  # 2->1，4->3

            # 结束本轮交换后，迭代prev_node为本次交换的尾
            prev_node = first_node  # 1，3
            head = first_node.next  # 3，null
        # 空结点指向头结点
        return e_node.next

# leetcode submit region end(Prohibit modification and deletion)
