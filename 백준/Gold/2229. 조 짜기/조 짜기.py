import sys
input = sys.stdin.readline


class Camp:
    def __init__(self, total_students, scores) -> None:
        self.total_students = total_students
        self.scores = scores

    def update_value(self, min_val, max_val, value):
        if value < min_val or value > max_val:
            return True
        return False

    def make_team(self):
        points = [0]*(self.total_students+1)
        for i in range(self.total_students):
            points[i+1] = points[i]
            j = i-1
            min_val = max_val = self.scores[i]
            while j >= 0 and self.update_value(min_val, max_val, self.scores[j]):
                min_val, max_val = min(
                    self.scores[j], min_val), max(self.scores[j], max_val)
                points[i+1] = max(points[i+1], points[j]+max_val-min_val)
                j -= 1
        return points[-1]


def init_data():
    total_students = int(input())
    scores = list(map(int, input().split()))
    return Camp(total_students, scores)


if __name__ == "__main__":
    camp_info = init_data()
    print(camp_info.make_team())
