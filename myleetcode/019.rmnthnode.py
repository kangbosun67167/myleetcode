# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        begin = head
        end = head

        while n>0:
            end = end.next
            n = n - 1
            if end == None and n >0:
                return None


        if end != None:
            while True:
                if end.next == None:
                    begin.next = begin.next.next
                    return head
                begin = begin.next
                end = end.next
        
        return head.next

if __name__ == "__main__":
    
    a = ListNode(1)
    # b = ListNode(2)
    # c = ListNode(3)
    # d = ListNode(4)
    # e = ListNode(5)

    # a.next  =b
    # b.next  =c
    # c.next  =d
    # d.next  =e

    tmp = a
    while True:
       
        if tmp == None:
            break
        print(tmp.val)
        tmp = tmp.next

    a = Solution().removeNthFromEnd(a,1)

    tmp = a
    while True:
       
        if tmp == None:
            break
        print(tmp.val)
        tmp = tmp.next

        