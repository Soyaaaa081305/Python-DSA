from stack import create_empty_stack, pop, push, is_empty

def evaluate_postfix(expression):
    stack = create_empty_stack()
    token = expression.split()
    
    for i in token:
        if i.isdigit():
            push(stack, int(i))
        else:
            right = pop(stack)
            left = pop(stack)
            
            if i == "+":
                result = left + right
            elif i == "-":
                result = left - right
            elif i == "*":
                result = left * right
            elif i == "/":
                result = left // right
            else:
                print("Hala mali operator mo")
            
            push(stack, result)
    return pop(stack)

exp = input("Enter an expression: ")
print(evaluate_postfix(exp))
