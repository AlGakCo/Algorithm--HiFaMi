# 소수 찾기

## 문제 설명

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

## 제한사핳
- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

## 입출력 예

|numbers|return|
|:---:|:-------:|
|17	|3|
|011|	2|

## 입출력 예 설명

예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

- 11과 011은 같은 숫자로 취급합니다.

## 문제풀이

```python
from itertools import permutations

def solution(numbers):

    first_list = []
    for number in numbers:
        first_list.append(number)

    all_list = []
    for i in range(1, len(first_list)+1):
        all_list += list(map(''.join, permutations(first_list, i)))

    all_list = list(map(int, all_list))
    all_list = set(all_list)
    count = 0

    for value in all_list:
        result = True
        for n in range(2, int(value)):
            if int(value)%n == 0:
                result = False
                break

        if result is True and (int(value) != 1 and int(value) != 0):
            count+=1

    return count
```

최초로 주어진 값을 나누어 `first_list`에 추가시킨다. 그 다음에 `itertools`의 `permutations`를 이용하여 각각 나올 수 있는 경우의 수를 뽑는다. 그리고 나서 `map`함수를 이용하여 `int` 타입으로 변경한 다음 `set`을 통하여 중복값을 제거한다. 마지막으로 소수일 경우를 판단하고 마지막 `count`가 되게 하기 위해서는 `0`또는 `1`이 아닌 수 만이 `count`되게 하여 그 수를 구한다.
