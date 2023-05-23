import sys
input = sys.stdin.readline


def init_data():
    total_switch = int(input())
    status = [False]+[True if int(x) == 1 else False for x in input().split()]
    total_student = int(input())
    students_list = [list(map(int, input().split()))
                     for _ in range(total_student)]

    return total_switch, status, students_list


def op_1(status, total_switch, num):  # 배수의 스위치 상태를 바꿈
    for i in range(num, total_switch+1, num):
        status[i] = not status[i]
    return status


def op_2(status, total_switch, num):  # 대칭인 스위치 상태를 바꿈
    pre = num - 1
    post = num + 1
    status[num] = not status[num]
    while (pre > 0) and (post <= total_switch):

        if status[pre] != status[post]:
            break

        status[pre] = not status[pre]
        status[post] = not status[post]
        pre -= 1
        post += 1

    return status


if __name__ == '__main__':
    total_switch, status, students_list = init_data()
    for student in students_list:
        if student[0] == 1:
            status = op_1(status, total_switch, student[1])
        if student[0] == 2:
            status = op_2(status, total_switch, student[1])

    for i in range(1, total_switch+1, 20):
        print(*list(map(int, status[i:i+20])))
