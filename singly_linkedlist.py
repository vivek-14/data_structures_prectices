from locale import currency
from os import link
import re


class Node:
    def __init__(self,data) -> None:
        self.data = data # Store data here
        self.next = None # Pointer here

class singlyLinkedList:
    def __init__(self) -> None:
        self.head = None # Head here

    def append(self, data):
        new_node = Node(data) # create new node
        if self.head is None:
            self.head = new_node # Assign new node to head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete_node_by_value (self, data):
        if self.head is None:
            return 
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def print_list(self):
        current = self.head
        while current:
            if current.next is not None:
                print(current.data, end="->")
            else:
                print(current.data)
            current = current.next

linked_list = singlyLinkedList()

linked_list.append(2) 
linked_list.prepend(3)
linked_list.prepend(1)
linked_list.append(6)
linked_list.delete_node_by_value(1)
print(linked_list.find(3))

linked_list.print_list()