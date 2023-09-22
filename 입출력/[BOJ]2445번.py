N = int(input())

for s in range(N):
    print('*' * (s+1), end = '')
    print(' ' * (N-s-1) , end = '')
    print(' ' * (N-s-1) , end = '')
    print('*' * (s+1))

for s in range(N-1,0,-1):
    print('*' * (s), end = '')
    print(' ' * (N-s) , end = '')
    print(' ' * (N-s) , end = '')
    print('*' * (s))
