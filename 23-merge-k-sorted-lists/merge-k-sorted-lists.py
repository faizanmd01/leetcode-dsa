# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a min-heap
        heap = []
        
        # Push the head of each non-empty linked list into the heap
        # We include 'i' (index) to avoid comparing ListNode objects directly 
        # when two nodes have identical values.
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
                
        dummy = ListNode(0)
        curr = dummy
        
        # Process the heap until it's empty
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Append the smallest node to our merged list
            curr.next = node
            curr = curr.next
            
            # If the popped node has a next node, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next