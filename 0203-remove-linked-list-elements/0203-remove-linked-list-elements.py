class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head is None:
            return None


        while head is not None and head.val == val:
            head = head.next

        current = head
        prev = None


        while current is not None:
            if current.val == val:
                # Remove the current node
                prev.next = current.next
            else:
                # Move to the next node
                prev = current
            current = current.next

        return head
