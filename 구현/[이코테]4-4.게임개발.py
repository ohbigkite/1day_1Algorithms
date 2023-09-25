# NxM 크기의 직사각형
# 캐릭터는 동서남북 중 한 곳을 바라본다
# 맵의 각 칸 - (A,B)
#- 현재 위치에서 왼쪽 방향부터 차례대로 갈 곳을 정한다
#- 왼쪽 방향에 가보지 않은 칸이 있으면 왼쪽 회전, 없으면 왼쪽 회전만하고 1로
#- 네 방향 모두 가본칸이거나 바다이면 방향 유지한채로 한칸 뒤
#- 방향 d : 0 = 북쪽, 1 = 동쪽, 2 = 남쪽, 3 = 서쪽
#- 셋째줄부터 맵이 육지인지 바다인지에 대한 정보 주어짐 : 0=육지, 1=바다 

N, M = map(int, input().split())
A, B, d = map(int, input().split())

# 게임 환경 맵 입력받기
array = []

for i in range(N):
    array.append(list(map(int, input().split())))

direction = [(-1,0),(0,1), (1,0), (0,-1)] # 반시계방향 서남동북

count = 1
turn_count = 0

dx = A
dy = B

for k in range(N * M):
    for s in range(4):
        ix = dx + direction[s-d][0] 
        iy = dy + direction[s-d][1]
        if array[ix][iy] == 0:
            dx = ix
            dy = iy
            array[ix][iy] = 1
            count += 1
            d = abs(3-turn_count)
            turn_count = 0
            break
        else:
            turn_count += 1

        if turn_count == 4:
            ix = dx + direction[1-d][0] # 북동남서 -> 북서남동으로 바라봐야함 
            iy = dy + direction[1-d][1]
            if array[ix][iy] == 0:
                dx = ix
                dy = iy
                array[ix][iy] = 1
                count += 1
                break
            
print(count)
        

