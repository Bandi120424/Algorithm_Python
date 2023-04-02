from itertools import combinations
from collections import Counter


def menu_combination(orders, course_num):
    """order에서 course_num 개의 메뉴로 구성된 조합을 리턴 

    Args:
        orders (_list_): 총 오더 리스트
        course_num (_int_): 메뉴 개수

    Returns:
        _list_: 메뉴 조합 리스트
    """
    menulist = []
    for order in orders:
        if len(order) < course_num:
            pass
        menulist += combinations(sorted(order), course_num)

    return menulist


def select_menu(menulist: list):
    """menu 조합 리스트에서 가장 주문 수가 많은 조합을 리턴
    (단, 최소 2회 이상 주문된 조합이어야 함)

    Args:
        menulist (list): 메뉴 조합 리스트

    Returns:
        list : 가장 주문 수가 많은 메뉴 조합 리스트 
    """
    selected_menu = []
    menulist_counter = Counter(menulist)
    max_order = max(menulist_counter.values())
    if max_order < 2:
        return []

    for menu in menulist_counter:
        if menulist_counter[menu] == max_order:
            selected_menu.append(''.join(menu))
    return selected_menu


def solution(orders, course):
    final_menu = []
    for num in course:
        menulist = menu_combination(orders, num)
        if len(menulist) > 0:  # menulist가 empty인 경우 주의
            final_menu += select_menu(menulist)
    final_menu.sort()
    return final_menu


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# menu_list = menu_combination(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], 5)
