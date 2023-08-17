import sys
input = sys.stdin.readline


def init_data():
    total_cases = int(input())
    word_list = [input().strip() for _ in range(total_cases)]
    return total_cases, word_list


def next_word(target: str = "") -> str:
    i = len(target)-2
    while i >= 0 and target[i] >= target[i+1]:
        i -= 1

    if i == -1:
        return target

    j = len(target)-1
    while target[i] >= target[j]:
        j -= 1

    return target[:i]+target[j]+''.join(reversed(target[i+1:j]+target[i]+target[j+1:]))


if __name__ == '__main__':
    total_cases, word_list = init_data()
    for word in word_list:
        print(next_word(word))
