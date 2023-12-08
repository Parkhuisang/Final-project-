def solution(numbers):
    # numbers를 문자열로 변환한 후, 문자열을 그대로 비교하여 정렬
    sorted_numbers = sorted(map(str, numbers), reverse=True)

    # 정렬된 문자열을 합쳐서 결과를 반환
    answer = str(int(''.join(sorted_numbers)))

    return answer

###
numbers = [8, 30, 17, 2, 23]
result = solution(numbers)
print(result)
