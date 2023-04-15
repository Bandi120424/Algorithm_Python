def correct_bracket(input_str=None):
    if input_str == None:
        raise Exception("Input: None")

    count = 0
    for ele in input_str:
        if ele == '(':
            count += 1
        else:  # elif ele == ')'
            count -= 1

        if count < 0:
            return False

    return True if count == 0 else False


def balanced_bracket(input_str=None):
    if input_str == None:
        raise Exception("Input: None")

    count = 0
    for ele in input_str:
        if ele == '(':
            count += 1
        else:  # elif ele == ')'
            count -= 1

    return True if count == 0 else False


def split_str(input_str=None):
    if input_str == None:
        raise Exception("Input: None")

    prestr, poststr = "", ""
    for idx in range(1, len(input_str)+1):
        if balanced_bracket(input_str[:idx]):
            prestr = input_str[:idx]
            poststr = input_str[idx:]
            break

    return prestr, poststr


def correction_process(input_str=None):
    if input_str == None:
        raise Exception("Input: None")

    if len(input_str) == 0:
        return ""

    prestr, poststr = split_str(input_str)
    if correct_bracket(prestr):
        return prestr+correction_process(poststr)

    new_poststr = "("+correction_process(poststr)+")"
    for c in prestr[1:-1]:
        if c == "(":
            new_poststr += ")"
        elif c == ")":
            new_poststr += "("
    return new_poststr


def solution(input_str):

    if correct_bracket(input_str):
        return input_str
    return correction_process(input_str)