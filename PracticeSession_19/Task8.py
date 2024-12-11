
class InsufficientBalanceException(Exception):
    pass

def check_value(value):
    Balance=100000
    if value > Balance:
        raise InsufficientBalanceException("Insufficient balance!!")
    else:
        print(f"{value} has been Debited from your account available balance is {Balance-value}")

try:
    num=int(input("Enter Amount to withdraw:"))
    check_value(num)
except InsufficientBalanceException as e:
    print(e)