# 10818
# 풀이1 - min, max 함수 이용
N = int(input())
K = list(map(int, input().split()))


print(min(K), max(K))

# 풀이2 - min max 직접

N = int(input())
K = list(map(int, input().split()))

min_ = K[0]
max_ = K[0]

for i in range(N):
    if K[i] > max_:
        max_ = K[i]
    if K[i] < min_:
        min_ = K[i]

print(min_, max_)
