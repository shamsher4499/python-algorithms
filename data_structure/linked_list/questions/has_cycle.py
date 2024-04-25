class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle_list(head):
    dummy = ListNode()
    dummy.next = head
    fast = slow = dummy

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def display_merge_list(head):
    show_list = ''
    current = head
    while current:
        show_list += "{}->".format(current.val)
        current = current.next
    return show_list