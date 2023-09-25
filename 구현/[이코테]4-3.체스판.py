# 미리 이동할 수 있는 방향 8가지를 배열에 저장해주기!
# 체스판은 8 X 8 크기 // 도착지가 체스판 안이면 경우의 수 +1

count = 0

now = input()
now_x = int(ord(now[0])) - int(ord('a')) + 1 
now_y = int(now[1])


steps = [(-2,-1), (-2,1), (2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]

for s in range(8):
    dx = now_x + steps[s][0]
    dy = now_y + steps[s][1]
    if (dx > 1 and dx < 8) and (dy > 1 and dy < 8) :
        count += 1

print(count)
