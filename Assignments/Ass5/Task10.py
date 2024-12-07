# Create a lambda function to sort a list of dictionaries by a specified key. For example,
# given students = [{"name": "Alice", "age": 24}, {"name": "Bob", "age": 22}, {"name": "Charlie", "age": 23}],
# sort the list by age using the lambda function.

students = [
    {"name": "Alice", "age": 24},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 23}
]
sorted_students = sorted(students, key=lambda student: student["age"])
print("Sorted by age:", sorted_students)
