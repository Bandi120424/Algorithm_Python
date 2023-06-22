import sys
input = sys.stdin.readline

CHARTONUM = {"ONE": '1', "TWO": '2', "THREE": "3", "FOUR": "4", "FIVE": "5",
             "SIX": "6", "SEVEN": "7",  "EIGHT": "8", "NINE": "9", "ZERO": "0"}


def init_data():
    total_cases = int(input())
    given_str = [[x for x in input().strip()] for _ in range(total_cases)]

    return total_cases, given_str


'''
ONE TWO THREE FOUR FIVE
SIX SEVEN EIGHT NINE ZERO

"X" SIX 
"G" EIGHT
"W" TWO
"Z" ZERO  
"U" FOUR
"R" THREE
-------- 이제 유일한 
"O" ONE
"F" FIVE
"S" SEVEN
"I" NINE
'''


def remove_char(keyword, words, target):
    numbers = ""
    for _ in range(target.count(keyword)):
        for w in words:
            target.remove(w)
        numbers += CHARTONUM[words]
    return numbers, target


def find_phone_num(target):
    phone_number = ""

    numbers, target_str = remove_char("X", "SIX", target)
    phone_number += numbers

    numbers, target_str = remove_char("G", "EIGHT", target_str)
    phone_number += numbers

    numbers, target_str = remove_char("W", "TWO", target_str)
    phone_number += numbers

    numbers, target_str = remove_char("Z", "ZERO", target_str)
    phone_number += numbers

    numbers, target_str = remove_char("U", "FOUR", target_str)
    phone_number += numbers

    numbers, target_str = remove_char("R", "THREE", target_str)
    phone_number += numbers

    numbers, target_str = remove_char("O", "ONE", target_str)
    phone_number += numbers

    numbers, target_str = remove_char("F", "FIVE", target_str)
    phone_number += numbers

    numbers, target_str = remove_char("S", "SEVEN", target_str)
    phone_number += numbers

    numbers, target_str = remove_char("I", "NINE", target_str)
    phone_number += numbers

    return sorted(phone_number)


if __name__ == '__main__':
    total_cases, given_str = init_data()
    for idx in range(total_cases):
        print(f"Case #{idx+1}: {''.join(find_phone_num(given_str[idx]))}")
