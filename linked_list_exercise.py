

class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None


    def print(self):
        if self.head is None:
            return 'Linked list is empty'
        
        itr = self.head
        l_list = ''
        while itr:
            l_list += str(itr.data)+'---->' if self.head.next else str(self.data)
            itr = itr.next

        return l_list
    
    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    
    def insert_at_beng(self, value):
        data = Node(value, self.head)
        self.head = data

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return 
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(value, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    

l_link_obj = LinkedList()
l_link_obj.insert_at_beng(3)
l_link_obj.insert_at_beng(4)
l_link_obj.insert_at_beng(5)
l_link_obj.insert_at_end(50)
l_link_obj.insert_at_end(90)

print(l_link_obj.print())
print(l_link_obj.get_length())

