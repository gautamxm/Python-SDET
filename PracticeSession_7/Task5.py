# Write a function called prime_numbers that takes two integers start and end and 
# returns a list of all prime numbers within that range (inclusive).

# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
primes = []

for num in range(2, 7):
    if num > 1:
        isPrime = True
        for i in range(2,num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(num)
# print(f"Prime numbers between {start} and {end}: {primes}")
print(primes)
