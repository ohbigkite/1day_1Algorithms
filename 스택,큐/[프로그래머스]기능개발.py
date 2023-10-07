from collections import deque

def solution(progresses, speeds):
    answer = []
    progress = deque(progresses)
    speed = deque(speeds)
    day = 0
    count = 0
    
    while len(progress) != 0:
        if (progress[0] + (speed[0] * day))  >= 100:
            progress.popleft()
            speed.popleft()
            count += 1
        else:
            if count >= 1:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)

    return answer