# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n1 = n2 = head
        while n!=0:
            n1 = n1.next
            n-=1
        if n1 is None:
            return head.next
        while n1.next:
            n1 = n1.next
            n2 = n2.next
        n2.next = n2.next.next
        return head