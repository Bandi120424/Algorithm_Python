import sys
input = sys.stdin.readline

seq_len, sequence_sum = map(int, input().split())
sequence = list(map(int, input().split()))

temp_seq = []
count = 0


def find_seq_with_sum(start_idx):
    global count
    if (len(temp_seq) > 0) and (sum(temp_seq) == sequence_sum):
        count += 1

    for idx in range(start_idx, seq_len):
        temp_seq.append(sequence[idx])
        find_seq_with_sum(idx+1)
        temp_seq.pop()


find_seq_with_sum(0)
print(count)