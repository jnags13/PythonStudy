# 01_variable.py

# 변수 생성 및 값 저장
# 1) 변수 = 값
result = 10
print(result)
result = 20
print(result)

# 2) 여러개의 변수에 여러개의 값을 저장 : , 를 이용해 변수명과 값을 나열 할 수 있음
a=1
b=2
c=3
d=4

# 변수명1, 변수명2, 변수명3 = 값,1 값2, 값3
# 변수명과 값이 위치 순서대로 대입이 됨
# 변수명의 갯수와 값의 갯수가 같아야 함
a,b,c,d = 1,2,3,4
print(a)
print(b)
print(c)
print(d)

# 3) 여러개의 변수에 한개의 값을 저장 : =를 계속 사용
# 변수명1 = 변수명2 = 변수명3 = 값
a = b = c = 10
print(a)
print(b)
print(c)

# 두 변수의 값 교환(swap) - 임시변수가 필요없음(다른언어와의 차이점
# 변수1, 변수2 = 변수2, 변수1
# a,b 변수에 10과 20의 값을 저장하고 a변수의 값을 b로 b 변수의 값을 a 로 옯기시오
a,b = 10,20
print(a,b)
a,b = b,a
print(a,b)

# 변수 삭제 : 변수는 ram(메모리)사용량과 직결되기 때문에 필요 없다고 판별되면 삭제 해야 함
# del 명령어 사용
# del 변수명

c = 100
print(c)
del c # 변수 c 삭제
#print(c) # 에러 발생 NameError: name 'c' is not defined
