# # 테스트 케이스 개수 입력
# T = int(input())  # 여러 테스트 케이스를 처리하기 위해 입력받음
#
# # 각 테스트 케이스 처리
# for t in range(1, T + 1):  # 테스트 케이스 번호는 1부터 시작
#
#     # 경로의 길이 N 입력
#     N = int(input())  # 경로의 길이를 입력받음
#
#     # 경로 정보 입력
#     path = list(map(int, input().split()))  # 경로를 구성하는 높이 정보를 리스트로 입력받음
#
#     # 완만한 오르막 길이 저장할 변수
#     best_length = 0  # 김싸피가 가장 좋아하는 오르막 길의 길이를 저장할 변수, 초기값은 0
#     min_slope = 99999999  # 경사도의 최소값을 저장할 변수, 초기값은 매우 큰 값으로 설정
#
#     i = 0  # 경로의 인덱스를 나타내는 변수, 초기값은 0
#     while i < N - 1:  # 경로의 끝까지 순회
#         if path[i] <= path[i + 1]:  # 오르막이 시작되는 지점을 찾음
#             start = i  # 오르막이 시작되는 위치를 기록
#             # 오르막이 끝날 때까지 계속 진행
#             while i < N - 1 and path[i] <= path[i + 1]:  # 오르막이 계속되는 동안 인덱스를 증가시킴
#                 i += 1
#             end = i + 1  # 오르막이 끝나는 지점의 다음 위치를 기록 (경로에서 다음 칸을 의미)
#
#             # 경사도 계산
#             A = path[end - 1]  # 오르막 길의 가장 높은 점(A)
#             B = path[start]  # 오르막 길의 가장 낮은 점(B)
#             C = end - start  # 오르막 길의 길이(C)
#             slope = (A - B) / C  # 경사도 계산, 경사도는 (A - B) / C로 계산
#
#             # 경사도가 더 낮거나, 경사도가 같지만 길이가 더 긴 경우 최적값 갱신
#             if slope < min_slope or (slope == min_slope and C > best_length):
#                 min_slope = slope  # 최소 경사도로 갱신
#                 best_length = C  # 최적 오르막 길의 길이로 갱신
#         else:
#             i += 1  # 오르막이 아닌 경우 다음 칸으로 이동
#
#     # 결과 출력
#     print(f'#{t} {best_length}')  # 테스트 케이스 번호와 함께 최적 오르막 길의 길이를 출력

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    path = list(map(int, input().split()))

    best_length = 0
    min_slope = 99999999999999999999999

    i = 0
    while i < N - 1:
        if path[i] <= path[i + 1]:
            start = i
            while i < N - 1 and path[i] <= path [i + 1]:
                i += 1
            end = i + 1

            A = path[end - 1]
            B = path[start]
            C = end - start
            slope = (A - B)/C

            if slope < min_slope or (slope == min_slope and C > best_length):
                min_slope = slope
                best_length = C

        else:
            i += 1

    print(f'#{t} {best_length}')






# 김싸피는 등산을 좋아해 주말마다 등산을 한다. 하지만 체력이 약한 김싸피는
# 최대한 완만한 경사도를 가지는 오르막 길을 좋아한다. 전체 경로 길이가 N인
# 경로에서 김싸피가 제일 좋아하는 오르막 길의 길이를 출력하는 프로그램을
# 작성하시오.
# - 등산 경로의 지형은 정수 배열 형태로 주어진다.
# - 오르막 길은 이전 위치 보다 높거나 같은 경우 계속 이어진다고 판단한다.
# - 경사도는 오르막길에서 가장 높은 높이 A 와 가장 낮은 높이 B의 차에서
# 경로 길이 C 를 나눈 값이다.예) 오르막길 경로가 [1, 3, 4, 5] 인 경우, A = 5,
# B = 1, C = 4 이므로 ( A – B ) / C = 1, 따라서 경사도는 1이다.
# - 만약 경사도가 같은 경우, 오르막 길이가 긴 경로의 길이를 출력한다.
# (경사도가 같은 경우에 대해 부동소숫점 수의 오차는 고려하지 않아도 된다.)


























