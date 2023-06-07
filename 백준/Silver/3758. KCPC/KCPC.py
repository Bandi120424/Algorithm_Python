import sys
input = sys.stdin.readline


def init_data():

    total_teams, total_problems, team_id, log_entry = map(int, input().split())

    # score, 제출 수, 마지막 제출 시간
    team_info = [[0, log_entry, 0] for _ in range(total_teams+1)]
    # team_ctn = {i: 0 for i in range(1, total_teams+1)}
    team_info_problem = [
        [0 for _ in range(total_problems+1)] for _ in range(total_teams + 1)]

    for t in range(log_entry):
        id, problem, score = map(int, input().split())
        team_info_problem[id][problem] = max(
            team_info_problem[id][problem], score)
        team_info[id][1] -= 1  # 제출횟수가 적은 팀이 우선순위
        team_info[id][2] = t

    for id in range(total_teams+1):
        team_info[id][2] = log_entry - team_info[id][2]
        team_info[id][0] = sum(team_info_problem[id])

    return team_info, team_id


def rank(team_info, team_id):
    score, ctn, time = team_info[team_id]
    team_info.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    return team_info.index([score, ctn, time])+1


if __name__ == '__main__':
    total_cases = int(input())
    for _ in range(total_cases):
        team_info, team_id = init_data()
        print(rank(team_info, team_id))
