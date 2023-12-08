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
