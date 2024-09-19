
# file_handling_assignment.py

# File Creation
def create_file():
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("The second line contains the number 123.\n")
        file.write("Finally, here's the third line with some text.\n")

# File Reading and Display
def read_file():
    with open("my_file.txt", 'r') as file:
        contents = file.read()
        print("File Contents:")
        print(contents)

# File Appending
def append_to_file():
    with open("my_file.txt", 'a') as file:
        file.write("This is an additional line 1.\n")
        file.write("Here comes another extra line 2.\n")
        file.write("And the last appended line 3.\n")

# Main function to run all tasks
def main():
    create_file()          # Create and write to the file
    read_file()            # Read and display the file contents
    append_to_file()       # Append more content to the file
    read_file()            # Read and display the file contents again

# Execute the script
if __name__ == "__main__":
    main()
