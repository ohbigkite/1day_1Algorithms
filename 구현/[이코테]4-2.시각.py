# 정수 N이 입력되면 0시00분00초~ N시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우의수



N = int(input())
count= 0

for i in range(N+1):
    for s in range(60):
        for j in range(60):
            if '3' in str(i) + str(s) + str(j) :
                count += 1

print(count)
