from stack import create_empty_stack, pop, push, is_empty

s = input("Enter a string: ")

splittedword = s.split()
result = []

for i in splittedword:
    stack = create_empty_stack()
    reversed_word = " "
    for char in i:
        push(stack, char)
    
    while not is_empty(stack):
        reversed_word += pop(stack)
    
    result.append(reversed_word)
print(" ".join(result))    