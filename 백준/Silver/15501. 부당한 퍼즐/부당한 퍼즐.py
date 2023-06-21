import sys
input = sys.stdin.readline


def init_data():
    total_number = int(input())
    seq1 = list(map(int, input().split()))
    seq2 = list(map(int, input().split()))

    return total_number, seq1, seq2


def good_or_bad(total_number, seq1, seq2):
    for i in range(total_number):
        if seq1[0] == seq2[i]:
            if seq1 == seq2[i:]+seq2[:i]:
                return "good puzzle"
            break

    seq1 = seq1[::-1]

    for i in range(total_number):
        if seq1[0] == seq2[i]:
            if seq1 == seq2[i:]+seq2[:i]:
                return "good puzzle"
            break

    return "bad puzzle"


if __name__ == '__main__':
    total_number, seq1, seq2 = init_data()
    print(good_or_bad(total_number, seq1, seq2))
