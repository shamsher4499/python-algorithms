'''
linked_list = 1->2->3->4->5
Output: 3->4->5

linked_list = 1->2->3->4->5->6
Output: 4->5->6
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return
    
    @property
    def display(self):
        list_node = ''
        head = self.head
        while head:
            list_node += f'{head.data}->'
            head = head.next
        return list_node
    
    @property
    def middle_value(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
    
def display_merge_list(head):
    show_list = ''
    current = head
    while current:
        show_list += "{}->".format(current.data)
        current = current.next
    return show_list

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    data = [1, 2, 3, 4, 5, 6]
    for d in data:
        linked_list.append(d)
    print(linked_list.display)
    print("Middle node")
    middle = linked_list.middle_value
    print(display_merge_list(middle))