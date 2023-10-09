### 문제풀이 핵심아이디어 또는 새롭게 알게된 내용: 2번째 for문에서 else문 break 추가 안 해줘서 틀렸었음! i가 ㅓ보다 작거나 같은 횟수를 세는게 아니라 기간을 세는 거기때문에 break를 써줘야 함!

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i,len(prices)-1):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                break
    
    return answer

