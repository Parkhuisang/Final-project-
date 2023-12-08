def solution(my_string, target):        # my_string에서 target이라는 부분 문자열이 포함되어 있는지 확인
    if target in my_string:             # 포함되어 있다면 answer 변수에 1을 할당
        answer = 1
    else:                               # 포함되었다면 answer 변수에 0을 할당
        answer = 0
    return answer

###
my_string = 'apple'
target = 'app'

result = solution(my_string, target)    # 결과를 result에 저장
print(result)                           # 결과 출력