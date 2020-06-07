# 숫자야구
## 문제 설명

숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다.

각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

```
* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃
```

예를 들어, 아래의 경우가 있으면

```
A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
```

이때 가능한 답은 324와 328 두 가지입니다.

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.

## 입출력 예

|baseball|return|
|:------:|:-----:|
|`[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]`|	2|

## 문제풀이

```python
def solution(baseball):
    result = []
    for i in range(123, 988):
        if len(set(str(i))) == 3 and not '0' in str(i):
            count = 0
            i = str(i)

            for base in baseball:
                strike = 0
                ball = 0
                first = str(base[0])
                for j in range(3):
                    if i[j] == first[j]:
                        strike += 1
                    elif i[j] != first[j] and i[j] in first:
                        ball += 1
                if base[1] == strike and base[2] == ball:
                    count += 1

            if count == len(baseball):
                result.append(i)
    return len(result)          
```
숫자는 무조건 3자리 수에다가 `중복`되는 수가 없어야 하고 또한 `0`이 들어가서는 안된다. 따라서 `set`을 통해 중복제거를 한 후, 그 길이가 무조건 `3`일때 즉, 중복되는 숫자가 없을 경우와 또한 `0`이 안들어 갔을 때의 수를 가지고 `baseball`로 주어지는 숫자와 규칙에 맞게 게임을 하여 스트라이크 수와 볼의 수가 같을 경우 `count`의 값이 증가하도록 하였다. `result`에 추가가 되기 위해서는 `count`와 `len(baseball)`의 수가 같아야 하는데 이는 질문의 개수와 `count`의 개수가 같게끔 하여 모든 질문을 통과하였음을 의미한다. 그 다음 `result`의 개수를 반환하면 그 값이 모든 질문을 통과한 수의 개수가 된다.
