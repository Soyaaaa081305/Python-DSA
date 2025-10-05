from stack import Stack

def main():
    stack = Stack()
    print("--- Simple Text Editor ---")
    print("Options: type, undo, view, history, exit")
    
    while True:
        cmd = input("Enter command: ").lower()

        match cmd:
            case "type":
                word = input("Enter word: ")
                stack.push(word)
                print(f"Added: {word}")

            case "undo":
                removed = stack.pop()
                if removed:
                    print(f"You’ve undone: {removed}")

            case "view":
                top_word = stack.peek()
                if top_word:
                    print(f"Top word: {top_word}")
                else:
                    print("Stack is empty.")

            case "history":
                print("History:")
                stack.display()

            case "exit":
                print("Exiting...")
                break

            case _:
                print("Invalid command.")
                

if __name__ == "__main__":
    main()
