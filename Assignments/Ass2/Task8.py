# 8.	Movie Ticket Pricing: Write a function that determines the ticket price based on the age of a person. If the person is under 12 years old, the price is $5. If the person is between 12 and 64, the price is $12. If the person is 65 or older, the price is $7. Return the ticket price as an integer.

def tprice(age):
    if age < 12:
        return 5
    elif 12 <= age <= 64:
        return 12
    else: return 7

age = int(input("Enter the age of the person: "))
price = tprice(age)
print(f"The ticket price for age {age} is: ${price}")