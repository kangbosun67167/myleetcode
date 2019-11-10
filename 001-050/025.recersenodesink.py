# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if k == 1:
            return head

        node_save = list()

        for i in range(k):
            times = i
            node = head
            while times>0:
                if node == None or node.next == None:
                    return head
                node = node.next
                times -= 1

            node_save.append(node)
        
        head = node_save[-1]
        node_save[0].next = self.reverseKGroup(node_save[-1].next,k)
        for i in range(1,k):
            node_save[i].next = node_save[i-1]
        
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

    d = Solution().reverseKGroup(d,1)

    node = d
    while node!= None:
        if node.val == None:
            break
        print(node.val)
        node = node.next

