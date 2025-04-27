# Error Handling Lab
try:
    # Ask the user for a filename
    filename = input("Enter the filename: ")

    # Try to open the file
    with open(filename, "r") as file:
        content = file.read()

    # Print the content if successful
    print("File content:")
    print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: The file could not be read.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
