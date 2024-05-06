import sys

def main():
    # Check if the name is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python name.py <your_name>")
        return

    # Extract the name from the command-line argument
    name = sys.argv[1]

    # Greet the user
    print"Hello, " + name + "! Welcome to Python.")

if __name__ == "__main__":
    main()
