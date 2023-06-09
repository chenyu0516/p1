import matplotlib.pyplot as plt
import random
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize


TEST_INDEX_x = 20
# How many steps the walking process in x-axis has.
TEST_INDEX_y = 20
# How many steps the walking process in y-axis has.
TEST_ROUNDS = 10000
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
    data_list = [[0 for _ in range(2*b+1)]for _ in range(2*a+1)]
    for i in range(TEST_ROUNDS):
        result = walking(a, b)
        data_list[a+result[0]][b+result[1]] += 1
    return data_list


if __name__ == '__main__':
    data = probability_test(TEST_INDEX_x, TEST_INDEX_y)
    print(data)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Normalize the data to range between 0 and 1
    # Normalize the data to range between 0 and 1
    norm = Normalize(vmin=0, vmax=max(map(max, data)))
    sm = ScalarMappable(norm=norm, cmap='viridis')

    for i in range(2 * TEST_INDEX_x + 1):
        for j in range(2 * TEST_INDEX_y + 1):
            if data[i][j] != 0:
                # Map the data value to a color using the ScalarMappable
                color = sm.to_rgba(data[i][j])
                ax.scatter(i - TEST_INDEX_x, j - TEST_INDEX_y, data[i][j], color=color)

    # The position of the colorbar
    cax = fig.add_axes([0.85, 0.15, 0.05, 0.7])  # [left, bottom, width, height]

    # Add the colorbar to the separate axis
    cbar = plt.colorbar(sm, cax=cax)
    cbar.set_label('Z-axis', fontsize=14)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()