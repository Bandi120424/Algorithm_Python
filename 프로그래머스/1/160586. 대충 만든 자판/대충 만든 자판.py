def keymap_dict(keymap):
    key_dict = {}
    for keys in keymap:
        for idx in range(len(keys)):
            if keys[idx] not in key_dict:
                key_dict[keys[idx]] = idx+1
            else:
                key_dict[keys[idx]] = min(key_dict[keys[idx]], idx+1)
    return key_dict

def solution(keymap, targets):
    answer = []
    key_dict = keymap_dict(keymap)
    for target_str in targets:
        key_stroke = 0
        for c in target_str:
            if c not in key_dict.keys():
                key_stroke = -1
                break 
            key_stroke += key_dict[c]
        answer.append(key_stroke)
    return answer