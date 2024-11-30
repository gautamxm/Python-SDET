# 14.	Implement a nested function that demonstrates how inner functions can access variables from the outer function.

def main():   
    var = 3
    def inner():
        print(var)
    inner() 
main()   


