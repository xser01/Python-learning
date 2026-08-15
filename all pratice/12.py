#206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before=None
        while head!=None:
            next=head.next
            head.next=before
            before=head
            head=next
        return before

#linkedlist:元素加指针，结构类似1－2－3－4－None，next，更改会丢失部分链表