## 풀이

def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else: answer += i.upper()
    return answer
  
  #해설
  #lower, upper만 알면 충분히 풀 수 있는 문제
