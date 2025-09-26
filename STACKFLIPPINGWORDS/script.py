from stack import create_empty_stack, push, pop, is_empty


stack = create_empty_stack()

# 2. Ask the user for a string
text = input("Enter a string: ")

# 3. Go through the string character by character
result = ""   # This will hold the final output
for ch in text:
    if ch != " ":    # If it's not a space, push the letter to the stack
        push(stack, ch)
    else:
        # If it's a space → pop all letters (reverses the word)
        while not is_empty(stack):
            result += pop(stack)
        result += " "   # Add the space back

# 4. At the end, pop any remaining letters (last word)
while not is_empty(stack):
    result += pop(stack)

# 5. Show the flipped words
print(result)
