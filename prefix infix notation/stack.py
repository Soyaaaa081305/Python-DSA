class Stack:
    def __init__(self):
        self.top = -1
        self.value = None
        self.next = None

def create_empty_stack():
    return Stack()

def is_full(stack, size=100):
    return stack.top == size - 1

def is_empty(stack):
    return stack.top == -1

def push(stack, item):
    if not is_full(stack):
        new_node = Stack()
        new_node.value = item
        new_node.next = stack.next
        stack.next = new_node
        stack.top += 1

def pop(stack):
    if not is_empty(stack):
        popped_node = stack.next
        stack.next = popped_node.next
        stack.top -= 1
        return popped_node.value
    return 0

def peek(stack):
    if not is_empty(stack):
        return stack.next.value
    return 0
