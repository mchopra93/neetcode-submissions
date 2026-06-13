# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        prev = ListNode(0)
        prev.next = head
        group_start = prev

        counter = 0
        num_rev = 0

        forw = head
        
        while counter<k and forw:
            temp = forw.next
            counter+=1
            
            if counter == k:
                rev = self.reverse(group_start.next,temp)
                old_group_start = group_start.next
                group_start.next = rev
                old_group_start.next = temp
                num_rev+=1
                counter = 0
                if num_rev == 1:
                    head = rev
                
                # Move group
                group_start = old_group_start
                prev = group_start
            
            forw = temp
        
        return head


    
    def reverse(self,head:Optional[ListNode],stop:Optional[ListNode]):

        prev = None
        forw = head
        while forw!=stop:
            temp = forw.next
            forw.next = prev
            prev = forw
            forw = temp
        return prev



        
        

        
        
        

        