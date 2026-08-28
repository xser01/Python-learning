#21,leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, link1: Optional[ListNode], link2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(None)
        now=head
        while link1:
            val1=link1.val
            while link2:
                val2=link2.val
                if val1>=val2:
                    now.next=link2
                    link2=link2.next
                    now=now.next
                else:
                    now.next=link1
                    link1=link1.next
                    now=now.next
                    break
        if link1 is None and link2 is not None:
            now.next=link2
        else:
            now.next=link1
        return head.next
#双指针题目，这里使用的是双while嵌套循环，时间复杂的为O（n＊m）
#注意的点：now＝now.next;now.next=now是两个不一样的意义


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listb=[]
        while list1:
            listb.append(list1.val)
            list1=list1.next
        while list2:
            listb.append(list2.val)
            list2=list2.next
        if not listb:
            return None
        listb.sort()
        head=ListNode(listb[0])
        a=head
        for i in listb[1:]:
            a.next=ListNode(i)
            a=a.next
        return head
#链表－列表－链表


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, link1: Optional[ListNode], link2: Optional[ListNode]) -> Optional[ListNode]:
        if not link1:
            return link2
        elif not link2:
            return link1
        head=ListNode(None)
        now=head
        while link1 and link2:
            if link1.val <= link2.val:
                now.next=link1
                now=now.next
                link1=link1.next
            else:
                now.next=link2
                now=now.next
                link2=link2.next
        now.next=link1 or link2
        return head.next
#最好的双指针写法