import sys
input = sys.stdin.readline

def init_data():
    total_courses, take_courses = map(int, input().split())
    lecture_info_sum1 = []
    lecture_info_sum2 = []
    lecture_info_sum3 = []

    for _ in range(total_courses):
        comm, algo, machine = map(int, input().split())
        lecture_info_sum1.append(comm+algo)
        lecture_info_sum2.append(comm+machine)
        lecture_info_sum3.append(algo+machine)
    return take_courses, lecture_info_sum1, lecture_info_sum2, lecture_info_sum3

def sorted_sum(lecture_list=None, take_courses: int = 0):
    if lecture_list == None:
        raise Exception("input is None")
    sorted_lecture_list = sorted(lecture_list, reverse = True)
    return sum(sorted_lecture_list[:take_courses])

if __name__ == "__main__":
    take_courses, lecture_info_sum1, lecture_info_sum2, lecture_info_sum3 = init_data()

    ability_sum1 = sorted_sum(lecture_info_sum1, take_courses)
    ability_sum2 = sorted_sum(lecture_info_sum2, take_courses)
    ability_sum3 = sorted_sum(lecture_info_sum3, take_courses)
    print(max(ability_sum1, ability_sum2, ability_sum3))
