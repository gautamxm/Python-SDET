# 3.	Write a function that opens a file, writes a list of numbers (1 to 10) into the file,
# and then closes it. Use a try-finally block to ensure the file is properly closed even if an exception occurs.

try:
    with open('data.txt', 'w') as file:
        numbers = list(range(1, 11))
        for number in numbers:
            file.write(f"{number}\n")
        print("Numbers written to the file successfully.")
finally:
    print("File is now closed.")