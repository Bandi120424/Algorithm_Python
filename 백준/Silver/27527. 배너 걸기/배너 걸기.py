import sys
import math
input = sys.stdin.readline


class Banner():
    def __init__(self, total_interval, banner_length, interval) -> None:
        self.total_interval = total_interval
        self.banner_length = banner_length
        self.interval = interval
        self.limit = int(math.ceil(9*self.banner_length/10))

    def init_interval_dict(self, sub_interval):
        interval_dict = {}
        for num in sub_interval:
            if num not in interval_dict:
                interval_dict[num] = 1
            else:
                interval_dict[num] += 1
        return interval_dict

    def update_interval_dict(self, start, idx, interval_dict):
        new_interval_dict = interval_dict
        new_interval_dict[self.interval[start]] -= 1

        val = self.interval[idx]
        if val in interval_dict:
            new_interval_dict[val] += 1
        else:
            new_interval_dict[val] = 1

        return new_interval_dict

    def over_limit(self, idx, interval_dict):
        if interval_dict[self.interval[idx]] >= self.limit:
            return True
        return False

    def can_install(self):
        interval_dict = self.init_interval_dict(
            self.interval[:self.banner_length])
        for val in interval_dict.values():
            if val >= self.limit:
                return "YES"

        start = 0
        for i in range(self.banner_length, self.total_interval):
            interval_dict = self.update_interval_dict(start, i, interval_dict)
            start += 1
            if self.over_limit(i, interval_dict):
                return "YES"

        return "NO"


if __name__ == "__main__":
    total_interval, banner_length = map(int, input().split())
    interval = list(map(int, input().split()))
    banner = Banner(total_interval, banner_length, interval)
    print(banner.can_install())
