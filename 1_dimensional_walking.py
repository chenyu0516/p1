import matplotlib.pyplot as plt
import random


TEST_INDEX = 50
# How many steps the walking process has.
TEST_ROUNDS = 10000
# Shows the result of how many times the walking process is performed.
P = 0.5
# The variable that determines the probability of going forward.


def walking(a):
    x = 0
    for i in range(a):
        if random.random() < P:
            x -= 1
        else:
            x += 1
    return x


def probability_test(a):
    data_list = [0] * (2 * a + 1)
    for _ in range(TEST_ROUNDS):
        result = walking(a)
        data_list[result + a] += 1
    return data_list


if __name__ == '__main__':
    data = probability_test(TEST_INDEX)
    fig = plt.figure()
    for i in range(TEST_INDEX + 1):
        plt.bar(i, data[TEST_INDEX + i], width=0.4, color='red')
        plt.bar(-i, data[TEST_INDEX - i], width=0.4, color='red')
    plt.show()