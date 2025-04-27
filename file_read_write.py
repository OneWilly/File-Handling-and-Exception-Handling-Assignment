# File Read & Write Challenge
try:
    # Read content from the input file
    with open("input.txt", "r") as input_file:
        content = input_file.read()

    # Modify the content (convert to uppercase in this example)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("output.txt", "w") as output_file:
        output_file.write(modified_content)

    print("File processed successfully! Check 'output.txt'.")
except Exception as e:
    print(f"An error occurred: {e}")
