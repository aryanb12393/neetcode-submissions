# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first_ptr = head

        if first_ptr.next is None:
            print("yo")
            return None
        
        prev = None
        second_ptr = head

        for i in range(n):
            first_ptr = first_ptr.next
        
        while first_ptr != None:
            first_ptr = first_ptr.next
            temp = second_ptr
            second_ptr = second_ptr.next
            prev = temp
            # prev = temp

        # print(first_ptr.val)
        print(second_ptr.val)

        if prev is not None:
            print("prev value")
            print(prev.val)
            prev.next = second_ptr.next

        # deleting the head
        else:
            head = second_ptr.next


        return head
        