import sys
input = sys.stdin.readline


def init_data():
    total_trees, taken_wood = map(int, input().split())
    tree_heights = list(map(int, input().split()))

    return total_trees, taken_wood, tree_heights


def find_height(total_trees, taken_wood, tree_heights):
    tree_heights.sort(reverse=True)
    min_height, max_height = 0, tree_heights[0]

    while min_height <= max_height:
        mid_height = (min_height+max_height)//2
        tree_sum = 0
        for idx in range(total_trees):
            if tree_heights[idx] > mid_height:
                tree_sum += tree_heights[idx] - mid_height
            else:
                break

        if tree_sum >= taken_wood:
            min_height = mid_height + 1
        else:
            max_height = mid_height - 1

    return max_height


if __name__ == '__main__':
    total_trees, taken_wood, tree_heights = init_data()
    print(find_height(total_trees, taken_wood, tree_heights))
