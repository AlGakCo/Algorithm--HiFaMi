# 전화번호 목록

## 문제설명

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

## 제한사항

- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.

## 입출력 예제

|phone_book	|return|
|:-------:|:-----:|
|`[119, 97674223, 1195524421]`|	false|
|`[123,456,789]`	|true|
|`[12,123,1235,567,88]`|false|

## 문제풀이
`solution_1`

```python
def solution(phone_book):
    phone_book = sorted(phone_book)

    pre_num = phone_book.pop(0)

    result = True
    for phone_number in phone_book:
        if pre_num in phone_number:
            result = False

    return result
```

`sorted`를 이용하여 접두사 번호가 제일 앞으로 나오도록 한 다음 `pop`을 이용하여 접두사 번호를 뽑았다.
그 다음에 `for` 루프를 이용하여 `phone_book` 리스트 안에 접두사 번호가 있을 경우 `result`는
`Fasle`를 반환하고 아닐경우 `default`값은 `True`를 반환한다.

`result` 변수에 값을 할당하지 않고 바로 `False`로 반환해도 상관없다. 바로 반환하는 경우가
조금 더 효율적일 것이다.

`solution_2`
```python
def solution(phone_book):
    phone_book = sorted(phone_book)

    pre_num = phone_book.pop(0)

    phone_book = tuple(phone_book)

    for num in phone_book:
        if num.startswith(pre_num, 0, len(pre_num)):
            return False
    return True
```

기본적으로는 `solution_1`과 비슷하지만 `solution_2`의 경우는 `startswith`를 사용해서
비교했다는 것이 다르다. `startswith`의 경우 3개의 인자를 받는데
`비교할 단어, 시작위치, 종료위치` 이다. 위의 코드에서 `시작위치, 종료위치`를 받는것과 안받는것에
대한 차이가 나지 않는다.
