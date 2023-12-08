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
