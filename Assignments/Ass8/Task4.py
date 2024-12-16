# 4.	Write a script to read lines from a file records.txt and
# print them to the console. Add exception handling to manage file not found and permission errors.

try:
    with open('records.txt', 'r') as file:
        for line in file:
            print(line, end='')

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You do not have permission to read the file.")

except Exception as e:
    print(f"Unexpected error: {e}")