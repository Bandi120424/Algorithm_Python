def factorial(number:int = 0) -> int:
    result = 1
    if number == 0 or number == 1:
        return result
    return number*factorial(number-1)
   
if __name__ == "__main__":
    number = int(input())
    print(factorial(number))
