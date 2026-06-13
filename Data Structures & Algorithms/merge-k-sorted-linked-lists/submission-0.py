# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if not lists:
            return None
        while k > 1:
            merged_lists = []
            for i in range(0,k,2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < k else None
                merged_lists.append(self.merge2Lists(l1,l2))
            lists = merged_lists
            k = len(lists)
        return lists[0]



    def merge2Lists(self, l1:Optional[ListNode], l2:Optional[ListNode]):

        head = ListNode(0)
        tail = head

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        return head.next

        
