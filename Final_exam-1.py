#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201903 이름 : 박희상

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

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

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }

    
    answer = ''

    
    morse_words = letter.split(' ')                # 공백을 기준으로 모스 부호를 나누어 리스트

    
    for morse_word in morse_words:                 # 각 모스 부호에 대응하는 영어 소문자를 찾아서 문자열에 추가
        if morse_word in morse:
            answer += morse[morse_word]

    return answer

###
letter = '.-.. .. ..-. .   - --- ---   ... .... --- .-. -'
result = solution(letter)
print(result)


# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGRAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    alphabet_values = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                       'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                       'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    
    
    age_str = str(age)              # age를 문자열로 변환하여 한 글자씩 처리
    
    
    answer = ''                     # answer 변수 초기화
    
    for char in age_str:        
        if char.isalpha():          #알파벳에 대응하는 값을 answer에 추가
            answer += str(alphabet_values[char])
        
    
    return int(answer)

###
age = 'programmer-857'
result = solution(age)
print(result)


# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

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
r1 = 2
r2 = 5
result = solution(r1,r2)
print(result)

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

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
