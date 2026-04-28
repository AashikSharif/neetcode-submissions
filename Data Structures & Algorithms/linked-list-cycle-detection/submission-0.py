# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()

        while head:
            if head not in nodeSet:
                nodeSet.add(head)
            elif head in nodeSet:
                return True
            head=head.next
        return False