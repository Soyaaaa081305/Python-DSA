from node import Node

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value) #we creating a newnode using node.py Node class and then we need value
        new_node.next = self.top # we need to point the new node to the to top of the stack
        self.top = new_node #changing the top pointer to point to the new node
        self.size +=1 #increasing the size

    def pop(self):
        if self.top is None:
            print("Empty stack uy")
            return -1 #for error daw to
        popped_value = self.top.value # so we can get the popped value bcs we cant return this later on eh
        self.top = self.top.next #moving the top pointer down,, so deletion na
        self.size = -1
        return popped_value #so we can see ano ung pinop na value

    def peek(self):
        if self.top is not None:
            return self.top.value
        print("alaws laman")

    def display(self):
        if self.top is None:
            print("empty ho")
        current = self.top
        print("dpende na kung ano gusto mong format")
        while current:
            print(current.value, endl = "")
            current = current.next
        print("alaws na")
        
            
            
        
