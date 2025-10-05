# script.py

from stack import Stack

def main():
    print("--- Browser Simulation ---")
    history = Stack()

    while True:
        print("\nOptions: visit, back, current, history, exit")
        command = input("Enter command: ").lower()

        if command == "visit":
            website = input("Enter website: ")
            history.push(website)
            print(f"Visited: {website}")

        elif command == "back":
            if history.is_empty():
                print("No previous website to go back to.")
            else:
                last = history.pop()
                now = history.peek()
                print(f"Went back from: {last}")
                if now:
                    print(f"Now at: {now}")
                else:
                    print("You are at a blank page.")

        elif command == "current":
            current_site = history.peek()
            if current_site:
                print(f"Currently viewing: {current_site}")
            else:
                print("No website currently open.")

        elif command == "history":
            history.display()

        elif command == "exit":
            print("Exiting browser...")
            break

        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
