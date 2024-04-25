

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def unknown_linked_list_function(head):
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def display_merge_list(head):
    show_list = ''
    current = head
    while current:
        show_list += "{}->".format(current.val)
        current = current.next
    return show_list


if __name__ == "__main__":
    linked_list1 = ListNode(1)
    linked_list1.next = ListNode(3)
    linked_list1.next.next = ListNode(5)
    linked_list1.next.next.next = ListNode(7)
    print('Linked list 1')
    print(display_merge_list(linked_list1))
    print('After reverse linked list:')
    head = unknown_linked_list_function(linked_list1)
    print(display_merge_list(head))