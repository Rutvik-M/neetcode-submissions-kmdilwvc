# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        tail=dummy
        min_heap=[]
        tie_breaker=0
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap,(lists[i].val,tie_breaker,lists[i]))
                tie_breaker+=1
        while min_heap:
            val,_,smallest_node=heapq.heappop(min_heap)
            tail.next=smallest_node
            tail=tail.next
            if smallest_node.next:
                heapq.heappush(min_heap,(smallest_node.next.val,tie_breaker,smallest_node.next))
                tie_breaker+=1
        return dummy.next
        