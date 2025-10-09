class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def is_empty(self):
        return self.top is None
#hi

while True:
    html_input = input("Enter HTML code (or type 'exit' to quit): ")
    if html_input.lower() == "exit":
        break

    stack = Stack()
    tag = ""
    inside = False
    valid = True

    for char in html_input:
        if char == "<":
            tag = ""
            inside = True
        elif char == ">":
            inside = False
            tag_content = tag.strip().lower()
            
           
            if tag_content.endswith("/"):
                continue
            
         
            tag_name = tag_content.split()[0].rstrip("/")
            
            if tag_name.startswith("/"): 
                if stack.is_empty() or stack.pop() != tag_name[1:]:
                    valid = False
                    break
            else:  
                stack.push(tag_name)
        elif inside:
            tag += char

    if valid and stack.is_empty():
        print("Valid")
    else:
        print("Invalid")
