# 8.	Create a class FileProcessor with methods to:
# •	Read a file.
# •	Write to a file.
# •	Append data to a file.

class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return f"Error: The file '{self.filename}' does not exist."
        except PermissionError:
            return f"Error: Permission denied to read the file '{self.filename}'."
        except Exception as e:
            return f"Unexpected error: {e}"

    def write_file(self, data):
        try:
            with open(self.filename, 'w') as file:
                file.write(data)
                return f"Data successfully written to '{self.filename}'."
        except PermissionError:
            return f"Error: Permission denied to write to the file '{self.filename}'."
        except Exception as e:
            return f"Unexpected error: {e}"

    def append_to_file(self, data):
        try:
            with open(self.filename, 'a') as file:
                file.write(data)
                return f"Data successfully appended to '{self.filename}'."
        except PermissionError:
            return f"Error: Permission denied to append to the file '{self.filename}'."
        except Exception as e:
            return f"Unexpected error: {e}"

filename = input("Enter the filename: ")
processor = FileProcessor(filename)

print("\nReading file content:")
print(processor.read_file())

new_data = input("\nEnter data to write to the file: ")
print(processor.write_file(new_data))

append_data = input("\nEnter data to append to the file: ")
print(processor.append_to_file(append_data))

print("\nReading updated file content:")
print(processor.read_file())

