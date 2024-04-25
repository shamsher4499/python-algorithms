
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList1:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         head = self.head
#         if not head:
#             self.head = new_node
#             return
#         current = head
#         while current.next:
#             current = current.next
#         current.next = new_node
#         return
    
#     def display(self):
#         show_list = ''
#         current = self.head
#         while current:
#             show_list += "{}->".format(current.data)
#             current = current.next
#         return show_list
    
# class LinkedList2:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         head = self.head
#         if not head:
#             self.head = new_node
#             return
#         current = head
#         while current.next:
#             current = current.next
#         current.next = new_node
#         return
    
#     def display(self):
#         show_list = ''
#         current = self.head
#         while current:
#             show_list += "{}->".format(current.data)
#             current = current.next
#         return show_list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def display_merge_list(head):
    show_list = ''
    current = head
    while current:
        show_list += "{}->".format(current.val)
        current = current.next
    return show_list

def merge_linked_list(head1, head2):
    current = ListNode()
    head = current

    while head1 and head2:
        if head1.val < head2.val:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next
    head.next = head1 or head2
    return current.next

# Example usage:
if __name__ == "__main__":
    linked_list1 = ListNode(1)
    linked_list1.next = ListNode(3)
    linked_list1.next.next = ListNode(5)
    linked_list1.next.next.next = ListNode(7)
    print('Linked list 1')
    print(display_merge_list(linked_list1))
    linked_list2 = ListNode(2)
    linked_list2.next = ListNode(4)
    linked_list2.next.next = ListNode(6)
    linked_list2.next.next.next = ListNode(8)
    print('Linked list 2')
    print(display_merge_list(linked_list2))
    print("Merging the two linked lists")
    head = merge_linked_list(linked_list1, linked_list2)
    print(display_merge_list(head))