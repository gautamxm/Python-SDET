
class strings:
    def reversed(self,str):
        print(str[::-1])
    def ispalindrome(self,str):
        ans = str[::-1]
        if ans == str:
            print("given string is palindrome")
        else: print("given string is not palindrome")