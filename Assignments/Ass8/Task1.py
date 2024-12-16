# 1.	Write a Python program that reads a file named data.txt. Use exception handling to manage the following scenarios:
# •	The file does not exist.
# •	The file is empty.
# •	Any unexpected error during file reading.

try:
    with open("data.txt", 'r') as file:
        content = file.read()

        if not content:
            raise ValueError("The file is empty.")
        print("File content:")
        print(content)

except FileNotFoundError:
        print("Error: The file does not exist.")

except ValueError as ve:
        print(f"Error: {ve}")

except Exception as e:
        print(f"Unexpected error: {e}")
