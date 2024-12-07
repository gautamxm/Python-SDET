# Write a program to add 30 days to the current date and print the result.

import datetime
current_date = datetime.datetime.now()
new_date = current_date + datetime.timedelta(days=30)

print("Current date:", current_date)
print("New date after adding 30 days:", new_date)
