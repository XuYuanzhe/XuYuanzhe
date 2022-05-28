"""
反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preview, current = None, head
        while current is not None:
            next = current.next
            current.next = preview
            preview = current
            current = next
        return preview


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5]
