from stack import create_empty_stack, pop, push

def infixtoprefix(expression):
    stack = create_empty_stack()
    expressions = expression[::-1]
    for token in expressions:
        if token.isalnum():
            push(stack, token)
        else:
            left = pop(stack)
            right = pop(stack)
            
            new_epression = f"({left} {token} {right})"
            push(stack, new_epression)
    return pop(stack)

            
            
        
    

exp = input("Input string here: ")
print(infixtoprefix(exp))

