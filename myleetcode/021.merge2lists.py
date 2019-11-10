# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l2.val < l1.val :
            l1,l2 = l2,l1 
        
        l1_point = l1
        l2_point = l2


        while True:
            
            if l1_point.next == None:
                l1_point.next = l2_point
                break
            if l2_point == None:
                break
            
            if l2_point.val < l1_point.next.val:
                tmp = l1_point.next
                l1_point.next = l2_point
                l2_point = l2_point.next
                l1_point = l1_point.next
                l1_point.next = tmp
            else:
                l1_point = l1_point.next            

        return l1

if __name__ == "__main__":
    
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next  =b
    b.next  =c
    c.next  =d
    d.next  =e

        
    a1 = ListNode(1)
    b1 = ListNode(2)
    c1 = ListNode(3)
    d1 = ListNode(4)
    e1 = ListNode(5)

    a1.next  =b1
    b1.next  =c1
    c1.next  =d1
    d1.next  =e1

    tmp = a
    while True:
       
        if tmp == None:
            break
        print(tmp.val)
        tmp = tmp.next

    a = Solution().mergeTwoLists(a,a1)

    tmp = a
    while True:
       
        if tmp == None:
            break
        print(tmp.val)
        tmp = tmp.next

        