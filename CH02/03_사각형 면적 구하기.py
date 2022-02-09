# 03_사각형 면적 구하기.py

# 사각형의 면적을 구하는 프로그램 v1
width = 100
helght = 200

area = width * helght

print("사각형의 면적은 : ", area)
print("사각형의 면적은 : " + str(area))


# 사각형의 면적을 구하는 프로그램 v2
# 사용자로부터 밑변과 높이를 입력받아 사각형의 넓이를 계산하는 프로그램
# 사용자로부터의 입력은 input() 기능을 사용한다.

print("사각형의 면적을 구하는 프로그램입니다. 밑변과 높이를 입력해주세요.")
width = int(input("밑변의 길이를 입력하세요. : ")) # 정수형변수
helght = int(input("높이를 입력하세요. : ")) # 정수형변수

print("입력한 밑변은 " + str(width) + "이고, " + "입력한 높이는 " + str(helght) + "입니다.")

area = width * helght

print("사각형의 면적은 : ", area)
print("사각형의 면적은 : " + str(area))