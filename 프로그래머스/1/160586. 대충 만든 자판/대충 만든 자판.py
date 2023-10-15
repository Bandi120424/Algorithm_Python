def keymap_dict(keymap):
    key_dict = {}
    for keys in keymap:
        for idx in range(len(keys)):
            if keys[idx] not in key_dict:
                key_dict[keys[idx]] = idx+1
            else:
                key_dict[keys[idx]] = min(key_dict[keys[idx]], idx+1)
    return key_dict

def count_keystroke(key_dict, target):
    key_stroke = 0
    for c in target:
        if c not in key_dict.keys():
            return -1 
        key_stroke += key_dict[c]
        
    return key_stroke 
    
def solution(keymap, targets):
    answer = []
    key_dict = keymap_dict(keymap)
    for target_str in targets:
        answer.append(count_keystroke(key_dict, target_str))
    return answer
