import sys
input = sys.stdin.readline


def init_data():
    total_pot, initial_moisture, watering_pot, moisture_gain = map(
        int, input().split())

    return total_pot, initial_moisture, watering_pot, moisture_gain


def watering(total_pot, initial_moisture, watering_pot, moisture_gain):
    pots = [initial_moisture] * total_pot

    days = 0
    while 0 not in pots:

        for i in range(watering_pot):
            pots[i] += moisture_gain-1

        for j in range(watering_pot, total_pot):
            pots[j] -= 1

        pots.sort()
        days += 1
    return days


def main():
    total_pot, initial_moisture, watering_pot, moisture_gain = init_data()
    print(watering(total_pot, initial_moisture, watering_pot, moisture_gain))


main()
