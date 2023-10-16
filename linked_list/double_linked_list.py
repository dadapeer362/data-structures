class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def create_DLL(self, value):
        new_node = Node(value)
        new_node.prev = None
        new_node.next = None
        self.head = new_node
        self.tail = new_node
        self.length += 1
        return "successfully created node"
    
    def insert_node(self, node_value, location):
        if not self.head:
            return "Node cannot be inserted"
        else:
            new_node = Node(node_value)
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == 1:
                new_node.next = None
                new_node.prev = self.tail
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

    def traverse_DLL(self):
        if not self.head:
            print("There is not any element to traverse")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next

    def reverse_traverse_DLL(self):
        if not self.head:
            print("There is not any element to traverse")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev

    def search_DLL(self, node_value):
        if not self.head:
            return "There is not any element in the list"
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                temp_node = temp_node.next
            return "The node value does not exist in the list"

    def delete_node(self, location):
        if not self.head:
            return "There is not any element in the list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            return "successfully deleted the node"
        
    def delete_DDL(self):
        if not self.head:
            print("There is not any node to delete")
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
        print("DLL has deleted successfully")     





doubleLL = DoubleLinkedList()
doubleLL.create_DLL(10)
doubleLL.create_DLL(20)
doubleLL.create_DLL(30)
doubleLL.create_DLL(40)
doubleLL.insert_node(15, 1)
doubleLL.insert_node(17, 1)
doubleLL.insert_node(18, 2)
doubleLL.traverse_DLL()
doubleLL.reverse_traverse_DLL()
print(doubleLL.search_DLL(18))
doubleLL.delete_node(2)
# doubleLL.delete_DDL()
print([node.value for node in doubleLL])