import sys
input = sys.stdin.readline


def init_data():
    seq1 = input().strip()
    seq2 = input().strip()

    return seq1, seq2


def find_lcs(seq1: str = "", seq2: str = ""):
    l1 = len(seq1)
    l2 = len(seq2)
    dp = [0]*l2  # dp[i]: seq1에서 i번째 index를 포함하는 LCS의 길이

    for i in range(l1):
        cnt = 0
        for j in range(l2):
            if cnt < dp[j]:
                cnt = dp[j]
                continue
            if seq1[i] == seq2[j]:
                dp[j] = cnt + 1

    return max(dp)


if __name__ == '__main__':
    seq1, seq2 = init_data()
    print(find_lcs(seq1, seq2))
