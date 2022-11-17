## 풀이

def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except:
            pass

    return answer
  
  #해설
  #정수형으로 표현하는 int()와 try except를 알아야 풀 수 있었다.
  #try:
  #  실행할 코드
  #except:
  #  예외가 발생했을 때 처리하는 코드
  
  #다른 해설
  
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer
#.isdigit()문자열이 '숫자'로만 이루어져있는지 확인하는 함수
#isdecimal()isdigit()isnumeric()
#.isalpha()문자열이 '알파벳'로만 이루어져있는지 확인하는 함수
