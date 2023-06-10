import matplotlib.pyplot as plt
import random


TEST_INDEX_x = 50
# How many steps the walking process in x-axis has.
TEST_INDEX_y = 50
# How many steps the walking process in y-axis has.
TEST_ROUNDS = 100
# Shows the result of how many times the walking process is performed.
P_x = 0.5
# The variable that determines the probability of going forward in x-axis.
P_y = 0.5
# The variable that determines the probability of going forward in y-axis.


def walking(a, b):
    x = 0
    y = 0
    for i in range(a):
        if random.random() < P_x:
            x -= 1
        else:
            x += 1
    for j in range(b):
        if random.random() < P_y:
            y -= 1
        else:
            y += 1
    return [x, y]


def probability_test(a, b):
    data_list_y = [0] * (2 * b + 1)
    data_list = [data_list_y] * (2 * a + 1)
    for _ in range(TEST_ROUNDS):
        result = walking(a, b)
        data_list[a+result[0]][b+result[1]] += 1
    return data_list


if __name__ == '__main__':
    data = probability_test(TEST_INDEX_x, TEST_INDEX_y)
    print(data)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    for i in range(2*TEST_INDEX_x+1):
        for j in range(2*TEST_INDEX_y+1):
            if data[i][j] != 0:
                ax.scatter(i-TEST_INDEX_x, j-TEST_INDEX_y, data[i][j])
    plt.show()
