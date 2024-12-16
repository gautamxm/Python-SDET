# 9.	Write a program to merge the contents of two files, file1.txt and file2.txt, into a third file merged.txt.
# Handle all possible exceptions during file operations.

try:
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    merged_file = 'merged.txt'
    with open(file1, 'r') as f1:
        content1 = f1.read()
    with open(file2, 'r') as f2:
        content2 = f2.read()
    with open(merged_file, 'w') as mf:
        mf.write(content1 + '\n' + content2)
    print(f"Contents successfully merged from '{file1}' and '{file2}' into '{merged_file}'.")

except FileNotFoundError as e:
    print(f"Error: One of the files was not found. {e}")
except PermissionError as e:
    print(f"Error: Permission denied to access the files. {e}")
except Exception as e:
    print(f"Unexpected error: {e}")