# Create two classes, EvenNumbers and OddNumbers, with a method generate_numbers(n)
# that generates the first n even or odd numbers.
# Write a function that takes an object of either class and prints the numbers

class EvenNumbers:
    def generate_numbers(self, n):
        even_numbers = []
        for i in range(n):
            even_numbers.append(i * 2)
        return even_numbers

class OddNumbers:
    def generate_numbers(self, n):
        odd_numbers = []
        for i in range(n):
            odd_numbers.append(i * 2 + 1)
        return odd_numbers

even = EvenNumbers()
print(even.generate_numbers(10))
odd = OddNumbers()
print(odd.generate_numbers(10))
