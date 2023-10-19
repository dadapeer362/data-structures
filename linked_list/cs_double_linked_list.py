class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create_CDLL(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
        return "Successfully created circular double linked list"
    
    def insert_node(self, value, location):
        if not self.head:
            return "The CDLL is not exist"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
            return "The node has beeen successfully inserted"
    
    def traverse(self):
        if not self.head:
            print("There is no CDLL exists")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next

    def reverse_traverse(self):
        if not self.head:
            print("There is no CDLL exists")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev

    def search(self, value):
        if not self.head:
            return "There is no CDLL exists"
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    return temp_node.value
                if temp_node == self.tail:
                    return "Value does not exist"
                temp_node = temp_node.next

    def delete_node(self, location):
        if not self.head:
            print("There is no CDLL exists")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            print("Successfully deleted the node")

    def delete_DLL(self):
        if not self.head:
            print("There is no CDLL exists")
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print("The CDLL has deleted successfully") 


circular_DLL = CircularDoubleLinkedList()
circular_DLL.create_CDLL(10)
circular_DLL.insert_node(20, 0)
circular_DLL.insert_node(30, 1)
circular_DLL.insert_node(40, 2)
circular_DLL.traverse()
circular_DLL.reverse_traverse()
print(circular_DLL.search(40))
circular_DLL.delete_node(2)
# circular_DLL.delete_DLL()
print([node.value for node in circular_DLL])