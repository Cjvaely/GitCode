# 反转一个单链表。
#
#  示例:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
#  进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#  Related Topics 链表

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :param head: ListNode
        :return: ListNode
        解法1：迭代
        遍历链表时，当前的next指向前一个元素，事先存储前一个元素，使用临时指针指向下一节点
        时间复杂度：O(n)，假设 是列表的长度，时间复杂度是 O(n)。
        空间复杂度：O(1).
        """
        # 当前结点
        prev = None
        current = head
        # 遍历链表
        while current:
            # 临时指针指向下一结点
            temp = current.next
            # 当前结点指向前一结点（第一个结点前一节点是None）
            current.next = prev
            # 当前结点成为前一结点
            prev = current
            # 当前结点指向下一结点
            current = temp
        return prev
    """
    解法2：递归
        出口：当前结点或者下一个结点为空
        内部：改变结点指向，head->next指向head递归函数
        参考：https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
        # 出口
        if head is None or head.next is None:
            return head
        # 此时node就是链表的最后一个结点（出口决定）
        # 以1->2->3->4->5为例，node最后得到的返回值就是5（反转链表后的头）
        node = self.reverseList(head.next)
        # 5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 返回头结点
        return node
    """









# leetcode submit region end(Prohibit modification and deletion)
