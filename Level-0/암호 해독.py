## 풀이

def solution(cipher, code):
    answer = ''
    for i in range(code,len(cipher)+1):
        if i % code == 0:
            answer+=cipher[i-1]
    return answer
    
# 해설
# 배수의 개념= 나누기가 0
