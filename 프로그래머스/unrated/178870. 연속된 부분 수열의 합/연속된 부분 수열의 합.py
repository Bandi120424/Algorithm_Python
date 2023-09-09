def solution(sequence, k):
    indexes = []
    seq_sum = 0
    left = 0
    right = -1
    
    while True:
        if seq_sum < k:
            right += 1
            if right >= len(sequence):
                break
            seq_sum += sequence[right]
        else:
            seq_sum -= sequence[left]
            if left >= len(sequence):
                break 
            left += 1
        if seq_sum == k:
            indexes.append([left, right])
        
    indexes.sort(key=lambda x: (x[1]-x[0], x[0]))
    return indexes[0]