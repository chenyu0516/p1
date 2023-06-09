import matplotlib.pyplot as plt
import random

test_index = 50
test_rounds = 10000
p = 0.5


def walking():
    global test_index
    x = 0
    for i in range(test_index):
        if random.random() < p:
            x -= 1
        else:
            x += 1
    return x


def probability_test():
    global test_index
    data_list = []
    for i in range(2 * test_index + 1):
        data_list.append(0)
    for i in range(test_rounds):
        result = walking()
        data_list[result+test_index] += 1
    return data_list


if __name__ == '__main__':
    data = probability_test()
    fig = plt.figure()
    for i in range(test_index+1):
        plt.bar(i, data[test_index+i], width=0.4, color='red')
        plt.bar(-i, data[test_index-i], width=0.4, color='red')
    plt.show()