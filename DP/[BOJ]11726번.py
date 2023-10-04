# 2xn크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수 구하기
# d[n] = d[n-1]+ d[n-2] 
# ex) 2x4직사각형은 2x3 직사각형 + 2x2 직사각형으로 생각하면됨
# ( 세세세 or 가가세 or 세가가)+ + (세세 or 가가)   


n = int(input())

d = [0] * (n+1)


if n == 1:
    print(1)

else:
    d[1] = 1
    d[2] = 3
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
        if i % 2 == 0:
            d[i]+=1
    
    print(d[n] % 10007)




