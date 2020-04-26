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
