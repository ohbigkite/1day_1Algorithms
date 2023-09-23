N = int(input())

for i in range(N,0,-1):
    print(' '* (N - i), end = '')
    print('*' * (2*i-1))
    #print(' '* (N - i), end ='')

for s in range(1,N):
    print(' '* (N - s-1), end = '')
    print('*' * (2*s + 1))

