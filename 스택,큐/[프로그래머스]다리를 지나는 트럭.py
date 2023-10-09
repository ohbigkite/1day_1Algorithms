#### 문제풀이 핵심아이디어 또는 새롭게 알게된 내용: in_bridge라는 현재 다리 상황 알려주는 queue를 만들고, 다리 무게 여유가 되면, 트럭을 추가해주고, 여유가 되지 않으면 무게가 0짜리인 트럭 넣어주기
#### 이때, sum함수를 쓰면 시간 초과되는 case 생기므로, 다리 무게 저장해주는 sum_bridge라는 변수 추가해주기! +) deque에 maxlen 설정해줘서 길이 제한해주기!

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    in_bridge = deque([0] * bridge_length, maxlen = bridge_length)
    truck_weight = deque(truck_weights)
    sum_bridge = 0
    
    while truck_weight or (sum(in_bridge)!=0): 
        answer += 1
        sum_bridge -= in_bridge[0]

        if (len(truck_weight) != 0) and (truck_weight[0] + sum_bridge <= weight):
            sum_bridge += truck_weight[0]
            in_bridge.append(truck_weight.popleft())
        else:
            in_bridge.append(0)
    
    return answer