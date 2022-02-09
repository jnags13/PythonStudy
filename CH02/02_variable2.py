# 02_variable2.py

# 문자열에 따옴표를 사용("",'')
name = "장석재"
age = 28

print(name, age) # 두 변수의 값을 한 라인에 출력

address = '서울시 마포구'

# print문에 문자열 또는 문자열 변수를 사용할 때 + 연산자를 이용하여 결합할 수 있음
# 변수 address 는 문자열 변수임
# '삽니다'는 문자열임
print(name + '는 ' + address + '에 삽니다')

# print문 또는 문자열의 결합 시 주의!!!
# 숫자는 결합 할 수 없다.
# print(name + '의 나이는' + age + '살 입니다.') TypeError: can only concatenate str (not "int") to str

# 형변환 : 현재의 데이터 형태를 일시적으로 다른 데이터로 형태를 변환시키는 것
# 숫자등의 객체를 문자로 변환 : str()
# 문자등의 객체를 숫자(정수)로 변환 : int()

print(name + '의 나이는 ' + str(age) + '살 입니다.')

# 문자 -> 숫자로 변환하는 예제, 10 진법을 기준으로 한 수치형 문자만 형변환이 가능함
k1 = '123'
k2 = '456'

print(k1 + k2)
print(int(k1) + int(k2))

#print(int(name) + 567) ValueError: invalid literal for int() with base 10: '장석재'