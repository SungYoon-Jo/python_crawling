string = 'I became a zombie'
 
# 한 문자씩 나누기 -> 리스트
list(string) # list() 함수 이용

 
 # 'a'를 구분자로 쪼갭니다.
 
print(string.split(' '))

# maxsplit은 최대 몇번 쪼갤지
# 처음 으로 나오는 공백 I 와 became사이를 쪼갭니다.

print(string.split(maxsplit=2))
 
# ## 다시 합칠 수도 있음
# (',').join(string.split()) # ','를 구분자로 합치기
 
# (' ').join(string.split()) # 공백을 구분자로 합치기 -> 원래 문자열
