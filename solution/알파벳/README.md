# 알파벳

## 문제

세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

## 입력

첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

## 출력

첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

| 입력 | 출력 |
|:----:|:-----:|
| 2 4<br>CAAB<br>ADCB | 3 |

## 풀이
이 문제의 경우 백트레킹 방식을 이용하여 문제에 접근하여야 한다. 하지만 그 방식이 어려워 검색을 통해 어떠한 방식으로 코딩을 해야하는지 도움을 받게 되었다.

```python
import timeit

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(x, y):
    global answer
    # x, y = list자리의 index
    # board = x, y에 대한 값
    q = set([(x, y, board[x][y])])

    # q가 존재 할 경우 while 루프를 돈다.
    while q:
        # x, y는 list의 index
        # ans는 거쳐온 list의 value 값
        x, y, ans = q.pop()

        # 위의 dx, dy값을 통해 자리 이동 좌, 하, 상, 우 순서
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx와 ny의 값이 OutOfRange가 아니고 board[nx][ny]의 값이 ans에 존재하지 않으면
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                # q의 vlaue에 x, y, ans에 board[nx][ny]의 value를 더함
                q.add((nx, ny, ans + board[nx][ny]))
                # answer는 그 전의 값, ans는 새로 받은값
                answer = max(answer, len(ans)+1)


def input_value():
    value = \
    """
2 4
CAAB
ADCB

    """
    value = value.strip().split("\n")

    index = value.pop(0).split(" ")

    value = index + value
    return value


if __name__ == "__main__":
    start_time = timeit.default_timer()
    value = input_value()
    R = int(value.pop(0))
    C = int(value.pop(0))
    board = [list(value.pop(0)) for _ in range(R)]

    answer = 1
    BFS(0, 0)
    print(answer)
    stop_time = timeit.default_timer()
    print(f"-------{round(stop_time-start_time, 7)} seconds-------")

```

위의 경우는 `BFS`방식을 사용한 경우이다. `BFS`는 너비 우선 탐색 방식으로, 루트 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법이다.

```
* 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법이다.
* 즉, 깊게(deep) 탐색하기 전에 넓게(wide) 탐색하는 것이다.
* 사용하는 경우: 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 선택한다.
  - Ex) 지구상에 존재하는 모든 친구 관계를 그래프로 표현한 후 Ash와 Vanessa 사이에 존재하는 경로를 찾는 경우
  - 깊이 우선 탐색의 경우 - 모든 친구 관계를 다 살펴봐야 할지도 모른다.
  - 너비 우선 탐색의 경우 - Ash와 가까운 관계부터 탐색
* 너비 우선 탐색(BFS)이 깊이 우선 탐색(DFS)보다 좀 더 복잡하다.
```
특징으로는
```
* 관적이지 않은 면이 있다.
  - BFS는 시작 노드에서 시작해서 거리에 따라 단계별로 탐색한다고 볼 수 있다.
* BFS는 재귀적으로 동작하지 않는다.
* 이 알고리즘을 구현할 때 가장 큰 차이점은, 그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검사 해야 한다는 것이다.
  - 이를 검사하지 않을 경우 무한루프에 빠질 위험이 있다.
```
[출처 - https://gmlwjd9405.github.io/](https://gmlwjd9405.github.io/2018/08/15/algorithm-bfs.html)
