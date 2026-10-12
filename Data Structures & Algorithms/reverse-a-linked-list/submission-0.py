# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        stack = []
        current = head
        
        while current:
            stack.append(current)
            current = current.next

        
        new_node = stack.pop()
        current = new_node
        while stack:
            node = stack.pop()
            current.next = node
            current = node

        
        current.next = None

        return new_node

        
        

        
            

