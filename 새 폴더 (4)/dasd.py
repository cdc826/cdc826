T = int(input())

# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 각 테스트 케이스 처리
for t in range(1, T + 1):
    # 실험판의 크기 N 입력
    N = int(input())

    # 실험판 정보 입력
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    # 최대 먹이 양을 저장할 변수
    max_food = -float('inf')

    # 모든 칸에 대해 계산
    for i in range(N):
        for j in range(N):
            # 현재 칸의 먹이 양을 포함하여 계산
            total_food = grid[i][j]

            # 상하좌우 인접 칸의 먹이 양 더하기
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:  # 유효한 칸인지 확인
                    total_food += grid[ni][nj]

            # 최대 먹이 양 갱신
            if total_food > max_food:
                max_food = total_food

    # 결과 출력
    print(f"#{t} {max_food}")