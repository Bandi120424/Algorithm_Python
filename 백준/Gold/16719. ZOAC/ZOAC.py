import sys
input = sys.stdin.readline

input_str = input().rstrip()

def words_reorder(words, char_idx):
    global words_in_order
    if not words:
        return

    min_char = min(words)
    min_char_idx = words.index(min_char)
    words_in_order[char_idx+min_char_idx] = min_char
    print(''.join(words_in_order))

    words_reorder(words[min_char_idx+1:],char_idx+min_char_idx+1)
    words_reorder(words[:min_char_idx],char_idx)

words_in_order = ['']*len(input_str)
words_reorder(input_str,0)