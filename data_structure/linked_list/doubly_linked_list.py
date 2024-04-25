class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
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
        new_node.prev = last_node

    def new_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def display(self):
        '''Display the linked list'''
        data_list = ''
        current = self.head
        while current:
            data_list += f"{current.data}"+"->"
            current = current.next
        return data_list

    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            current = None
            return
        while current.next.data != data:
            current = current.next
        current.next = current.next.next
        current.next.prev = current

# Example usage:
if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    data = [1, 2, 3, 4, 5]
    for d in data:
        doubly_linked_list.append(d)
    print(doubly_linked_list.display())
    print("\nAdding new head")
    doubly_linked_list.new_head(0)
    print(doubly_linked_list.display())