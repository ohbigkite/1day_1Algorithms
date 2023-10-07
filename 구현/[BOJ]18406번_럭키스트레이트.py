# 18406번 럭키스트레이트
# 반으로 나누어서 각 자리수 합을 더했을 때 똑같으면 럭키 스트레이트!
# 정수 n은 항상 짝수로 들어감!

n = input()
front = 0
back = 0

for i in range(n):
    if (i+1) < (n // 2):
        front += int(n[i])
    else:
        back += int(n[i])  

if front == back:
    print("LUCKY")
else:
    print("READY")
