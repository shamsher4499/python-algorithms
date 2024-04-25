class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_list(head, k):
    if not head or k == 0:
        return head

    # Find the length of the linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Adjust k to be within the range of the list length
    k = k % length

    if k == 0:
        return head

    # Find the new tail and new head
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head

def display_list(head):
    list_data = ''
    current = head
    while current:
        list_data += f"{current.val}->"
        current = current.next
    return list_data

# Test the function
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
print("Original list:")
print(display_list(head))
print(f"Rotate list by {k}")
rotated_head = rotate_list(head, k)
print(display_list(rotated_head))
