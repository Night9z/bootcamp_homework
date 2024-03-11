from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head
        
        # Dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize the pointers
        curr = head
        prev = dummy
        nex = None
        
        # Count the number of nodes in the list
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        # Iterate over the list and reverse the nodes in k groups
        while count >= k:
            curr = prev.next
            nex = curr.next
            for i in range(1, k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            count -= k
        
        return dummy.next

# Example usage:
# Assuming you have a linked list created and pointed by `head`,
# and you have assigned a value to `k`, you can call the function as follows:

# sol = Solution()
# new_head = sol.reverseKGroup(head, k)
