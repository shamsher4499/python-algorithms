class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def new_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
        return
    

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    data = [1, 2, 3, 4, 5]
    for d in data:
        linked_list.append(d)
    print(linked_list.display())
    print("\nAdding new head")
    linked_list.new_head(0)
    print(linked_list.display())
    print("\nDeleting 5")
    linked_list.delete(5)
    print(linked_list.display())

