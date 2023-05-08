import sys
from itertools import combinations
input = sys.stdin.readline


def init_data():
    password_len, total_alphabet = map(int, input().split())
    alphabet = [c for c in input().strip().split()]
    return password_len, sorted(alphabet)


def vowel_consonant_idx(alphabet):
    vowel_idx = []
    consonant_idx = []
    for i in range(len(alphabet)):
        if alphabet[i] in {'a', 'e', 'i', 'o', 'u'}:
            vowel_idx.append(i)
        else:
            consonant_idx.append(i)
    return vowel_idx, consonant_idx


def idx_sub(parent, child):
    return [item for item in parent if item not in child]


def passwords(password_len, alphabet):
    pwd_list = set([])
    alphabet_idx = [i for i in range(len(alphabet))]
    vowel_idx, consonant_idx = vowel_consonant_idx(alphabet)
    # print(alphabet)
    for v in vowel_idx:
        for c1, c2 in combinations(consonant_idx, 2):
            rest_idxes = combinations(
                idx_sub(alphabet_idx, [v, c1, c2]), password_len - 3)
            for case in rest_idxes:
                pwd = ""
                for i in sorted([v, c1, c2] + list(case)):
                    pwd += alphabet[i]
                pwd_list.add(pwd)

    return sorted(list(pwd_list))


if __name__ == "__main__":
    password_len, alphabet = init_data()
    for case in passwords(password_len, alphabet):
        print(case)
