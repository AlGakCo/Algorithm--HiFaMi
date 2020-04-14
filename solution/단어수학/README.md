# 단어수학

## 문제

민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.

N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

## 입력

첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다.

## 출력

| 입력 | 출력 |
|:-----:|:-----|
| 2<br>AAA<br>AAA | 1998 |
| 2<br>GCF<br>ACDEB | 99437 |
| 10<br>A<br>B<br>C<br>D<br>E<br>F<br>G<br>H<br>I<br>J | 45 |
| 2<br>AB<br>BA | 187 |

## 풀이

`solution1`
```python
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
```

`solution2`
```python
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
```
`solution2`의 경우 뒤부터 `reverse`하여 계산하도록 했지만 이럴경우 만약 10의 자리의 값과 1000의 자리의
값과 같다면 10의 자리의 낮은 값으로 1000의 자리의 값이 결정되기 때문에 `solution2`의 경우는 실패하게 된다.
