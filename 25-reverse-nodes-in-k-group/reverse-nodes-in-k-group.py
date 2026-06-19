# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node to safely handle the head of the modified list
        dummy = ListNode(0)
        dummy.next = head
        
        # This pointer tracks the node right before the current k-group
        group_prev = dummy
        
        while True:
            # 1. Find the k-th node from group_prev
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break  # If there aren't enough nodes left, leave them as is
            
            # Record the start of the next k-group
            group_next = kth.next
            
            # 2. Reverse the current k-group
            # 'prev' starts at group_next because the first node of this group 
            # will eventually point to the start of the next group
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # 3. Relink the reversed group into the main list
            # Store the current head of the group (which is now the tail)
            temp = group_prev.next
            # Connect the preceding group's tail to the new head of this group
            group_prev.next = kth
            # Move group_prev to the tail of the current group
            group_prev = temp
            
        return dummy.next

    def getKthNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr