# . Explain positional and keyword arguments in Python functions.
# Provide a code example that includes both types of arguments.
# task- 6
# Create a function personal_info that takes a name and age as positional arguments and an optional keyword argument city.
# If the city argument is not provided, the function should assume the city is "Unknown".
# Write sample calls for each possible way of calling this function


def personal_info(name,age,city="ambala"):
    print(f"Name : {name}, Age : {age}, City : {city}")

personal_info("Gautam", 23)
personal_info("Lucifer", 30, city="Rajpura")
personal_info("Aniket", 23, city="Patiala")
personal_info(name="Jay", age=35, city="Anni")
personal_info(name="Pushkar", age=40)


