# 바로 뒤 인덱스와 값 비교한 다음에 값이 다르면, answer에 append!
# 가장 마지막 인덱스는 항상 추가해주도록 예외처리!
# for문이 마지막 인덱스에는 안 돌아가게 설정하고, arr.pop()으로 마지막 인덱스값 추가해줄 수도 있음!

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == (len(arr)-1):
            answer.append(arr[i])
        elif arr[i] != arr[i+1] :
            answer.append(arr[i])
        else:
            continue
    return answer

