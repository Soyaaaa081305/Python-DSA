class Stack:
    def __init__(self):
        self.top = 0
        self.value = None
        self.next = None

def create_empty_stack():
    new_stack = Stack()
    new_stack.top = -1
    return new_stack

def is_full(stack, size=100):
    return stack.top == size - 1

def is_empty(stack):
    return stack.top == -1

def push(stack, item):
    if not is_full(stack):
        next_node = stack.next
        new_node = Stack()
        new_node.value = item
        new_node.next = next_node
        stack.next = new_node
        stack.top += 1

def pop(stack):
    if not is_empty(stack):
        first_node = stack.next
        stack.next = first_node.next
        stack.top -= 1
        return first_node.value
    return None

def peek(stack):
    if not is_empty(stack):
        return stack.next.value
    return None
