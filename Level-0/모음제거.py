## 풀이

def solution(my_string):
    tae=['a','e','i','o','u']
    
    for i in tae:
        my_string = my_string.replace(i, '')
    return my_string
  
  #해설
  #.replace()와 for 문으로 모음에 해당하는 aeiou를 
  
  #다른 해설
  
def solution(my_string):
    answer = ''

    for c in my_string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            continue
        answer += c

    return answer
