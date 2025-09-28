from stack import create_empty_stack, pop, push, is_empty

def implemented(exp):
    stack = create_empty_stack()
    for token in exp.split():
        if token.isdigit():
            push(stack, int(token))
        else:
            right = pop(stack)
            left = pop(stack)
            
            if token == "+":
                push(stack, left + right)
            elif token == "-":
                push(stack, left - right)
            elif token == "*":
                push(stack, left * right)
            elif token == "/":
                push(stack, left // right)
    return pop(stack)
        
        
    


exp = input("Enter a postfix string: ")
print(implemented(exp))