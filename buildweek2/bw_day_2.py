#Leetcode
#Intersection of two linked lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
def getListLen(head: ListNode) -> int:
    count = 0
    
    p = head
    
    while p is not None:
        count += 1
        p = p.next
        
    return count
    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
​
        # Keep current pointers per list
        pa = headA
        pb = headB
        
        # Grab list lengths and compute the difference
        len_a = getListLen(headA)
        len_b = getListLen(headB)
        
        len_diff = len_a - len_b
        
        # Skip len_diff nodes in the longer list
        if len_diff != 0:
            nodes_to_skip = abs(len_diff)
            
            for _ in range(nodes_to_skip):
                if len_diff > 0:  # list A is longer
                    pa = pa.next
                else:             # list B is longer
                    pb = pb.next
            
        # Move pointers lockstep, see when they become the same
        while pa is not None:
            if pa is pb:
                return pa
            
            pa = pa.next
            pb = pb.next
        
        # If we get here, no intersection found
        return None
    
        """
        seen = set()
        
        p = headA
        
        # Add all list A nodes to a set
        while p is not None:
            seen.add(p)
            p = p.next
            
        # Run through list B looking for seen nodes
        p = headB
        
        while p is not None:
            if p in seen:
                return p
            
            p = p.next
            
        # If we got here, we didn't find an intersection
        return None
        """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        visited = set()
        
        # Walk the entire linked list
        while cur is not None:
            
            # Check to see if we found a loop
            if cur in visited:
                return True
            
            # Mark as visited and move to the next
            visited.add(cur)
            cur = cur.next
            
        # If we get here, no loop was detected
        return False
   

