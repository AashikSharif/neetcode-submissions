# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow  =  head.next,head
        
        #To find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reversing  2nd half
        right = slow.next
        slow.next = None
        prev = None

        while right:
            tmp = right.next
            right.next = prev
            prev = right
            right = tmp


        #merge 
        left = head
        right = prev
        while  right:
            temp =  left.next
            temp2 = right.next

            left.next = right
            right.next = temp

            left= temp
            right = temp2







