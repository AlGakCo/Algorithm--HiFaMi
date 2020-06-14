# 카펫

## 문제설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

## 제한사항

- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
- 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

## 입출력 예

|brown|yellow|return|
|:----:|:----:|:----:|
|10|2|[4, 3]|
|8|1|[3, 3]|
|24|24|[8, 6]|

## 문제풀이

어떤 방식으로 풀어야 할 지 몰라 방법을 찾다보니 수학적인 공식이 있었다.

`width = brown+yellow`, `width = m * n`, `yellow = (m-2)*(n-2)`
위의 공식을 이용하여 문제를 풀게 되면 아래와 같이 나오게 된다.

```python
def solution(brown, yellow):

    empty_list = []
    width = brown + yellow

    for i in range(width, 0, -1):

        if width%i == 0:
            empty_list.append(i)

    for j in empty_list:
        m = j
        n = width/j

        if m >= n and (m-2)*(n-2) == yellow:
            return [m, n]  
```

이 방법은 위와 같은 식을 이용하여 코딩을 하였지만 가장 간단하게 풀었다고 생각되어 가져오게 되었다.

```python
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

```
