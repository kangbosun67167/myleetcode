# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

 

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        elif head.next == None:
            return head

        _next = head.next
        head.next  =  Solution().swapPairs(head=_next.next)
        _next.next = head
        head = _next
        return head

if __name__ == "__main__":
    a2 = ListNode(6)
    a1 = ListNode(5)
    a = ListNode(4)
    b = ListNode(3)
    c = ListNode(2)
    d = ListNode(1)

    d.next = c
    c.next = b
    b.next = a
    a.next = a1
    a1.next = a2

    # value = -1
    node = d
    while node!= None:
        if node.val == None:
            break
        print(node.val)
        node = node.next

    d = Solution().swapPairs(d)

    node = d
    while node!= None:
        if node.val == None:
            break
        print(node.val)
        node = node.next
