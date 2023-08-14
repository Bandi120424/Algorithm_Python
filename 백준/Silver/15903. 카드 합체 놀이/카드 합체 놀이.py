import sys
import copy
from collections import deque
input = sys.stdin.readline

'''
정렬을 하고, 적은 숫자부터 수행 
숫자를 더할 때, 두 수의 인덱스가 서로 달라야함에 주의!

'''

class cards():
    def __init__(self, num_of_cards: int = 0, card_status=None) -> None:
        self.num_of_cards = num_of_cards
        if card_status == None:
            raise Exception(
                f"{sys._getframe().f_code.co_name}: There are no cards")
        self.card_status = card_status

    def final_score(self, new_card_status):
        return sum(new_card_status)

    def merge_cards(self, total_actions):
        for _ in range(total_actions):
            self.card_status.sort()
            merged_num = self.card_status[0] + self.card_status[1]
            self.card_status[0] = merged_num
            self.card_status[1] = merged_num
        return self.final_score(self.card_status)


def init_data():
    num_of_cards, total_actions = map(int, input().split())
    card_status = list(map(int, input().split()))
    return total_actions, cards(num_of_cards, card_status)


if __name__ == "__main__":
    total_actions, card = init_data()
    print(card.merge_cards(total_actions))
