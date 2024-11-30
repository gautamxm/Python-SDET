num = int(input("Enter a number for prime factorization: "))
factors = []

while num % 2 == 0:
    factors.append(2)
    num = num // 2

i = 3
while i * i <= num:
    while num % i == 0:
        factors.append(i)
        num = num // i
    i+= 2

if num > 2:
    factors.append(num)

print(f"Prime Factors are: {factors}")