class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def display_linked_list(head):
    show_list = ''
    current = head
    while current:
        show_list += "{}->".format(current.val)
        current = current.next
    return show_list

'''
head = 1->2->3->4->
after dummy
0->1->2->3->4->
ahead: 4.next
before: 0.next
'''

def remove_n_node(head, n):
    dummy = ListNode()
    dummy.next = head
    ahead = before = dummy

    for _ in range(n+1):
        ahead = ahead.next

    while ahead:
        before = before.next
        ahead = ahead.next

    before.next = before.next.next

    return dummy.next

if __name__ == "__main__":
    linked_list1 = ListNode(1)
    linked_list1.next = ListNode(3)
    linked_list1.next.next = ListNode(5)
    linked_list1.next.next.next = ListNode(7)
    print('Linked list 1')
    print(display_linked_list(linked_list1))
    head = remove_n_node(linked_list1, 2)
    print('After remove 2nd from last')
    print(display_linked_list(head))