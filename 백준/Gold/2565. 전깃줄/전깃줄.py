import sys
input = sys.stdin.readline


class Wires:
    def __init__(self, total_wires: int = 0, wires=None) -> None:
        if total_wires > 0 and wires == None:
            raise Exception(
                f"{self.__class__} {sys._getframe().f_code.co_name}: there is no wire")

        self.total_wires = total_wires
        self.wires = wires

    def remove_wire(self):
        remained_wires = [1] * self.total_wires
        if self.wires == None:
            raise Exception(
                f"{self.__class__} {sys._getframe().f_code.co_name}: there is no wire")

        ordered_wires = sorted(self.wires)
        for i in range(self.total_wires):
            for j in range(i):
                if ordered_wires[j][1] < ordered_wires[i][1]:
                    remained_wires[i] = max(
                        remained_wires[i], remained_wires[j]+1)
        return self.total_wires - max(remained_wires)


def init_data():
    total_wires = int(input())
    wires = [list(map(int, input().split())) for _ in range(total_wires)]

    return Wires(total_wires, wires)


if __name__ == "__main__":
    wires = init_data()
    print(wires.remove_wire())
