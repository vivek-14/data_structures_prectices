from ast import While
from tkinter import NO
from typing import Optional


class Node:
    def __init__(self, data:int) -> None:
        self.data: int = data
        self.next: Optional['Node']= None
        self.prev: Optional['Node'] = None

class doublyLinkedList:
    def __init__(self) -> None:
        self.head:Optional[Node] = None

    def append(self, data:int)-> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next: # Traverse to last node
                current_node = current_node.next
            current_node.next = new_node # point last nodes to new node
            new_node.prev = current_node # point back new node to last node
            print("---------------------Append-------------------------")
            print(f"Current node {current_node} = new_node.previous {new_node.prev}")
            print(f"New_node {new_node} = Current_node.next {current_node.next} ")

    def prepend(self, data:int)-> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            print("--------------------Prepend-------------------------")
            print(f"Current head {self.head} = new_node.next {new_node.next}")
            print(f"New_node {new_node} = Current_node.previous {self.head.prev} ")
            print(type(self))

    def insert_at_position(self, data:int, pos:int, choice:str = 'pre') -> None: # choices are ['pre', 'post']
        

        # Initial list check for append or prepend operation
        if self.head is None or pos > self.get_size():
            self.append(data)
            return

        if self.head.next is None or pos <= 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current: Optional[Node] = self.head
        current_position:int = 0

        if choice.lower() == 'pre':
            while current and current_position < pos:
                current_position += 1
                previous_node: Node = current
                current = current.next

            if current_position == pos:
                previous_node.next = new_node
                new_node.prev = previous_node
                new_node.next = current
                if current:
                    current.prev = new_node
            else:
                print('Position Out of bound appending at the end of list')
                self.prepend(data)
                
        if choice.lower() == 'post':
            while current and current_position <= pos: # [2,3,4,5]
                current_position +=1 # 3
                next_node: Node = current # 4
                current = current.next # 5
            
            if current_position == pos + 1:
                print(current_position, pos)
                next_node.next = new_node
                new_node.prev = next_node
                new_node.next = current
                if current:
                    current.prev = new_node                
            else:
                print('Position Out of bound appending at the end of list')
                self.append(data)  
    
    def print_list(self):
        current_node: Optional[Node] = self.head
        while current_node.next:
            print(current_node.data, end="<->")
            current_node = current_node.next
        print(current_node.data)

    def get_size(self) -> int:
        """Return the size (number of nodes) of the list."""
        count: int = 0
        current: Optional[Node] = self.head
        while current:
            count += 1
            current = current.next
        return count

linked_list = doublyLinkedList()

linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.prepend(2) 

linked_list.insert_at_position(10, 2, 'post')
linked_list.insert_at_position(9, 2, 'pre')

linked_list.print_list()
