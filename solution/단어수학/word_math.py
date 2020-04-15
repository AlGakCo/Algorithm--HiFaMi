
import timeit
from collections import Counter
from itertools import zip_longest

def solution(value):
    lenth = int(value.pop(0))
    value = sorted(value, key=len, reverse=True)

    word_dict = {}
    count = 9

    max_lenth = len(value[0])

    for i in range(1, lenth):
        if len(value[i]) != max_lenth:
            value[i] = "0"*(max_lenth-len(value[i])) + value[i]

    for i in range(max_lenth):
        for j in range(lenth):
            if value[j][i].isdigit() == False:
                if value[j][i] not in word_dict:
                    word_dict[value[j][i]] = count
                    value[j] = value[j].replace(value[j][i], str(count))
                    count -= 1

                else:
                    value[j] = value[j].replace(value[j][i], str(word_dict[value[j][i]]))

    answer = 0
    for i in value:
        answer += int(i)

    return print(answer)

def solution2(values):
    lenth = int(values.pop(0))

    for i in range(lenth):
        values[i] = values[i][::-1]

    values = sorted(values, key=len, reverse=True)
    max_lenth = len(values[0])

    result = []
    for value in values:
        result+=Counter(value)

    start_num = 10-len(result)+1
    word_dict = {}

    for i in range(max_lenth):
        for j in range(lenth):
            try:
                if values[j][i].isdigit() == False:
                    if values[j][i] not in word_dict:
                        word_dict[values[j][i]] = start_num
                        values[j] = values[j].replace(values[j][i], str(start_num))
                        start_num+=1
                    else:
                        values[j] = values[j].replace(values[j][i], str(word_dict[values[j][i]]))
            except IndexError:
                pass

    for i in range(lenth):
        values[i] = values[i][::-1]

    answer = 0
    for i in values:
        answer+= int(i)
    print(answer)

def solution2_1(values):
    lenth = int(values.pop(0))

    for i in range(lenth):
        values[i] = values[i][::-1]

    values = sorted(values, key=len, reverse=True)
    max_lenth = len(values[0])

    result = []
    for value in values:
        result+=Counter(value)

    start_num = 9
    word_dict = {}

    for i in reversed(range(max_lenth)):
        for j in range(lenth):
            try:
                if values[j][i].isdigit() == False:
                    if values[j][i] not in word_dict:
                        word_dict[values[j][i]] = start_num
                        values[j] = values[j].replace(values[j][i], str(start_num))
                        start_num-=1
                    else:
                        values[j] = values[j].replace(values[j][i], str(word_dict[values[j][i]]))
            except IndexError:
                pass

    for i in range(lenth):
        values[i] = values[i][::-1]

    answer = 0
    for i in values:
        answer+= int(i)
    print(answer)

def input_value():
    value = \
    """
    2
AB
BA
    """
    return value.replace(" ", "").strip().split("\n")









if __name__ == "__main__":
    start_time = timeit.default_timer()
    input_value = input_value()
    solution2_1(input_value)
    stop_time = timeit.default_timer()
    print(f"-------{round(stop_time-start_time, 7)} seconds-------")
