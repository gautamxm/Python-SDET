# 10.	Create a function process_file(file_path) that reads a file and returns the total number of words in it.
# Handle exceptions for missing file, empty file, and encoding errors.

def process_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content:
                raise ValueError("The file is empty.")
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except UnicodeDecodeError:
        print(f"Error: Encoding issue while reading the file '{filename}'.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

filename = input("Enter the file path: ")
word_count = process_file(filename)
if word_count is not None:
    print(f"The total number of words in the file is: {word_count}")
