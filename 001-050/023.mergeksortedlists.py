# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
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
            
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        out_list = lists[0]
        for list_single in lists[1:]:
            out_list = mergeTwoLists(out_list,list_single)

        return out_list
