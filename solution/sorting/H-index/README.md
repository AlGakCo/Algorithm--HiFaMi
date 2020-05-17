# H-index

## 문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

## 제한사항
- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

## 입출력 예

|citations|	return|
|:-------:|:------:|
|`[3, 0, 6, 1, 5]`|	3|

## 입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

## 문제풀이
문제에 대해 이해가 잘 안가서 다른 사람들이 해설 한 내용을 참고하였다.

이 문제의 경우
```
h번 이상 인용된 h개의 논문이 있으면 이때의 h를 리턴하면 됩니다.
3번 이상 인용된 논문이 4개 있으면 3을 리턴하고,
4번 이상 인용된 논문이 3개 있으면 3을 리턴합니다.
```
이해한 바로는 h가 h개의 논문 이상이 있는 값을 리턴하라는 것 같다.

```python
def solution(citations):

    citations = sorted(citations)

    answer = len(citations)
    while True:
        cnt = 0
        for citation in citations:
            if citation >= answer:
                cnt += 1
            if answer <= cnt:
                return answer
        answer -= 1

```
첫번째 코드는 `sorted`를 오름차순으로 하여 진행 하였다.

```
테스트 1 〉	통과 (0.89ms, 10.9MB)
테스트 2 〉	통과 (3.29ms, 10.7MB)
테스트 3 〉	통과 (1.76ms, 10.9MB)
테스트 4 〉	통과 (1.47ms, 10.7MB)
테스트 5 〉	통과 (2.80ms, 10.9MB)
테스트 6 〉	통과 (3.76ms, 10.8MB)
테스트 7 〉	통과 (0.28ms, 10.7MB)
테스트 8 〉	통과 (0.04ms, 10.7MB)
테스트 9 〉	통과 (0.05ms, 10.7MB)
테스트 10 〉	통과 (0.46ms, 10.8MB)
테스트 11 〉	통과 (5.10ms, 10.8MB)
테스트 12 〉	통과 (0.06ms, 10.8MB)
테스트 13 〉	통과 (2.89ms, 10.9MB)
테스트 14 〉	통과 (2.30ms, 10.8MB)
테스트 15 〉	통과 (3.78ms, 10.9MB)
테스트 16 〉	통과 (0.04ms, 10.8MB)
```

```python
def solution(citations):

    citations = sorted(citations, reverse=True)

    answer = len(citations)
    while True:
        cnt = 0
        for citation in citations:
            if citation >= answer:
                cnt += 1
            else:
                break

            if answer <= cnt:
                return answer
        answer -= 1
```
두번쨰의 경우는 `sorted` 할 때 `reverse` 옵션을 주어 내림차순으로 하고 만약 값이 `answer`의 값 미만이 되었을 경우 바로 루프를 `break`하고 다음 번으로 넘어가도록 하였다.

```
테스트 1 〉	통과 (0.88ms, 10.8MB)
테스트 2 〉	통과 (3.19ms, 10.8MB)
테스트 3 〉	통과 (1.65ms, 10.8MB)
테스트 4 〉	통과 (1.45ms, 10.8MB)
테스트 5 〉	통과 (2.78ms, 10.8MB)
테스트 6 〉	통과 (3.64ms, 10.9MB)
테스트 7 〉	통과 (0.29ms, 10.7MB)
테스트 8 〉	통과 (0.05ms, 10.7MB)
테스트 9 〉	통과 (0.05ms, 10.8MB)
테스트 10 〉	통과 (0.48ms, 10.8MB)
테스트 11 〉	통과 (4.89ms, 10.8MB)
테스트 12 〉	통과 (0.07ms, 10.7MB)
테스트 13 〉	통과 (2.85ms, 10.9MB)
테스트 14 〉	통과 (2.26ms, 10.8MB)
테스트 15 〉	통과 (3.68ms, 10.9MB)
테스트 16 〉	통과 (0.04ms, 10.7MB)
```

시간을 비교하였을 때 그리 많은 시간이 차이가 나지 않는다. 하지만 만약 `citations`의 길이가 길어졌을 경우 코드가 돌아가는 시간이 줄어들 것이라고 예상한다.
