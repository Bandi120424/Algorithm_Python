from collections import Counter

def add_topping(piece: dict, topping: str):
    """piece에 topping을 추가  

    Returns:
        list: topping이 추가된 piece 
    """
    if topping not in piece:
        piece[topping] = 1
    else:
        piece[topping] += 1
    return piece

def remove_topping(piece: list, topping: str):
    """piece에서 topping을 제거  

    Returns:
        list: topping이 제거된 piece 
    """
    piece[topping] -= 1 
    if piece[topping] == 0:
        del piece[topping]
    return piece

def solution(topping):
    answer = 0
    topping_dic = Counter(topping)

    first_piece = {}
    for i in range(len(topping)-1):
        first_piece = add_topping(first_piece, topping[i])
        topping_dic = remove_topping(topping_dic, topping[i])

        if len(first_piece) == len(topping_dic):
            answer += 1
            
    return answer
