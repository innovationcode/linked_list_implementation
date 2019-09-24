# LinkedList node
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data):    #insert at the end of the list
        node_to_insert = Node(data)
        if(self.head is None):
            self.head = node_to_insert

        elif(self.head is not None):
            current = self.head
            while current.next:
                current = current.next
            self.tail = node_to_insert    
            current.next = node_to_insert
        return self.head
    
    def print_tail(self):
      print(self.tail.data)

    def insert_at_start(self, data):
        node_to_insert = Node(data)
        if self.head is None:
            self.head = node_to_insert
        else:
            node_to_insert.next = self.head
            self.head = node_to_insert
        return self.head
    
    def insert_in_between(self, data, position):
        self.node_position = 0 
        node_to_insert = Node(data)
        if self.head is None:
            self.head = node_to_insert
            #self.node_position += 1
            return self.head
            
        elif self.head is not None:
            current = self.head
            while current.next:
                if (self.node_position + 1) == position:
                    break
                else:
                    current = current.next
                    self.node_position += 1 
            
        store_next = current.next
        current.next = node_to_insert
        node_to_insert.next = store_next
        
        return self.head
    
    def print(self):
        current = self.head
        while(current):
            print(current.data, end = " -> ")
            current = current.next
        
    def check_palindrome(self):
        current = self.head
        stack = []
        while(current):
            stack.append(current.data)
            current = current.next
        
        stack_reverse = stack[::-1]
        if stack == stack_reverse:
            print("PALINDROME")
        else:
            print("NOT PALINDROME....")
            
        
                
    
ll = Linkedlist()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.print_tail()
ll.insert_at_end(20)
ll.insert_at_end(10)
ll.check_palindrome()
ll.insert_at_start(250)
ll.insert_in_between(880, 4)
ll.check_palindrome()
print(ll.print())