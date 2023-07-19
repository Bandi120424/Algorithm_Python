import sys
import math
input = sys.stdin.readline

INF = 10000


def init_data():
    points = list(map(int, input().split()))
    return points


def gradient(points):
    grads = set([])

    if points[0] == points[2]:
        grads.add(INF)
    else:
        grads.add((points[3]-points[1])/(points[2]-points[0]))  # AB기울기

    if points[4] == points[0]:
        grads.add(INF)
    else:
        grads.add((points[5]-points[1])/(points[4]-points[0]))  # AC기울기

    if points[4] == points[2]:
        grads.add(INF)
    else:
        grads.add((points[5]-points[3])/(points[4]-points[2]))  # BC기울기

    if len(grads) != 3:
        return False

    return True


def compute_distance(A, B):
    x1, y1 = A
    x2, y2 = B
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


def distance(points):
    dist = []
    dist.append(compute_distance(
        (points[0], points[1]), (points[2], points[3])))  # AB
    dist.append(compute_distance(
        (points[0], points[1]), (points[4], points[5])))  # AC
    dist.append(compute_distance(
        (points[4], points[5]), (points[2], points[3])))  # BC

    return dist


def make_parallelogram(points):

    if gradient(points) == False:
        return -1

    dist = distance(points)
    rounds = []
    rounds.append(2*(dist[0]+dist[2]))
    rounds.append(2*(dist[0]+dist[1]))
    rounds.append(2*(dist[1]+dist[2]))

    return max(rounds) - min(rounds)


if __name__ == '__main__':
    points = init_data()
    print(make_parallelogram(points))
