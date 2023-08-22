import sys
input = sys.stdin.readline

def action(stack=None, command: int = 0, num: int = 0):
    if stack == None:
        raise Exception("Stack is empty")
        
    if command == 1:
        stack.append(num)
        return stack
    
    if command == 2:
        print(-1) if len(stack) == 0 else print(stack.pop())
        return stack 

    if command == 3:
        print(len(stack))
        return stack 
    
    if command == 4:
        print(1) if len(stack) == 0 else print(0)
        return stack

    if command == 5:
        print(-1) if len(stack) == 0 else print(stack[-1])
        return stack
    
    return stack 

if __name__ == "__main__":
    total_commands = int(input())
    stack = []
    for _ in range(total_commands):
        commands = list(map(int, input().split()))
        if len(commands) == 1:
            stack = action(stack, commands[0])
        else:
            stack = action(stack, commands[0], commands[1])
        