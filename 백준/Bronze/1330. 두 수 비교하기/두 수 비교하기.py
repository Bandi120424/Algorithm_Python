def init():
    num1, num2 = map(int, input().split())
    return num1, num2

def compare(num1: int = 0, num2: int = 0):
    if num1 > num2:
        return '>'
    if num1 < num2:
        return '<'
    if num1 == num2:
        return "=="
    
if __name__ == "__main__":
    num1, num2 = init()
    print(compare(num1, num2))