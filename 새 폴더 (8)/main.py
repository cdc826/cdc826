# T = int(input())
#
# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# for t in range(1, T + 1):
#     N = int(input())
#     grid = []
#     for _ in range(N):
#         grid.append(list(map(int, input().split())))
#
#     max_food = -9999999999999999
#
#     for i in range(N):
#         for j in range(N):
#             food = grid[i][j]
#
#             for di, dj in dir:
#                 ni, nj = i + di, j + dj
#                 if 0 <= ni < N and 0 <= nj < N:
#                     food += grid[ni][nj]
#
#             if food > max_food:
#                 max_food = food
#
#     print(f'#{t} {max_food}')




T = int(input())

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, T + 1):
    N = int(input())

    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    max_food = -99999999999999999

    for i in range(N):
        for j in range(N):
            food = grid[i][j]

            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0<= ni < N and 0<= nj < N:
                    food += grid[ni][nj]

            if food > max_food:
                max_food = food

    print(f'#{t} {max_food}')














































