# 时间复杂度：O（m+n）.while迭代了2个链表
# 空间复杂度：O（1）
from Week1.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1.设置哨兵节点，作为返回结果使用
        dummy = ListNode(-1)
        # 2.设置pre移动的头节点
        pre = dummy
        # 3.迭代2个链表
        while l1 and l2:
            # 4.由于链表是顺序当，将链表头部值较小当链表链接到pre.next
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            # 5.更新pre位置
            pre = pre.next
        # 6.对while结束时，把剩余的非空链表进行追加
        pre.next = l2 if l1 is None else l1
        # 7.哨兵节点的下一个，即为结果
        return dummy.next
