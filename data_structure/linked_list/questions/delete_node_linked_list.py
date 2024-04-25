class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(head, val):
    if head.val == val:
        head = head.next
        return head
    current = head
    while current.next is not None:
        if current.next.val == val:
            current.next = current.next.next
            return head
        current = current.next
    return head

def display_merge_list(head):
    show_list = ''
    current = head
    while current:
        show_list += "{}->".format(current.val)
        current = current.next
    return show_list

# Example usage:
if __name__ == "__main__":
    linked_list1 = ListNode(1)
    linked_list1.next = ListNode(3)
    linked_list1.next.next = ListNode(5)
    linked_list1.next.next.next = ListNode(7)
    print('Linked list 1')
    print(display_merge_list(linked_list1))
    print("\nDeleting 5")
    linked_list1 = delete_node(linked_list1, 6)
    print(display_merge_list(linked_list1))