# 7.	Create a script to copy content from one file to another.
# Handle exceptions for missing source file, permission errors, and other unforeseen issues.

try:
    source = input("Enter the source filename: ")
    destination = input("Enter the destination filename: ")
    with open(source, 'r') as source_file:
        content = source_file.read()
    with open(destination, 'w') as destination_file:
        destination_file.write(content)
    print(f"Content successfully copied from '{source}' to '{destination}'.")

except FileNotFoundError:
    print("Error: The source file does not exist.")
except PermissionError:
    print("Error: Permission denied when accessing the files.")
except Exception as e:
    print(f"Unexpected error: {e}")