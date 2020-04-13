
import timeit

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


def input_value():
    value = \
    """
    2
AAA
AAA
    """
    return value.replace(" ", "").strip().split("\n")









if __name__ == "__main__":
    start_time = timeit.default_timer()
    input_value = input_value()
    solution(input_value)
    stop_time = timeit.default_timer()
    print(f"-------{round(stop_time-start_time, 7)} seconds-------")
