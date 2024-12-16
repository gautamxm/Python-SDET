# 5.	Create a Python program that takes a filename as input and writes user-provided data into it. Handle exceptions for:
# •	Invalid filename input (e.g., blank filename).
# •	Permission denied when writing to the file.


try:
    filename = input("Enter the filename to write to: ")
    if not filename:
        raise ValueError("Filename cannot be blank.")
    data = input("Enter the data to write to the file: ")
    with open(filename, 'w') as file:
        file.write(data)
        print(f"Data successfully written to file")

except ValueError as ve:
    print(f"Error: {ve}")
except PermissionError:
    print(f"Error: You do not have permission to write to the file.")
except Exception as e:
    print(f"Unexpected error: {e}")