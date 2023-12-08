def solution(r1, r2):
    answer = 0
    distance = r1-r2                    # 두 원 중심 간의 거리
    
    if distance > 0:                    # 두 원의 중심 간의 거리가 양수일때

        answer = 4*(distance+1)         # 각사분면을 포함(*4), 각 원 위의 점 포함(+1)

    elif distance == 0:                 # 두 원의 크기가 같을 때

        answer = 4

    elif distance < 0:                  # 두 원의 중심 간의 거리가 음수일때

        answer = -(distance-1)*4        # 각사분면을 포함(*4), 각 원 위의 점 포함(-1)


    
    return answer


###
r1 = 7
r2 = 5
result = solution(r1,r2)
print(result)