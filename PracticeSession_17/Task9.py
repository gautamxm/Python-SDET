
class bankaccount:
    __accno = 90
    __balance = 90000
    def deposit(self,val):
        self.__balance += val
        print(f"Available Balance : {self.__balance}")
    def withdrawn(self,val):
        if 0 < val < self.__balance:
            self.__balance -= val
        print(f"Available Balance : {self.__balance}")

obj = bankaccount()
obj.deposit(10000)
obj.withdrawn(50000)
