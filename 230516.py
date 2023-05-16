'''
# 문제 : 다음 소스 코드를 완성하여 날짜와 시간을 출력하시오.
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, )
print(hour, minute, second, )


출력
2019/04/26 11:34:27
'''

# 답 1
# 오답 : 이유- 공백처리
print(year, '/', month,'/', day, end = " " )
print(hour, ':', minute, ':', second )
# 2019 / 04 / 26 11 : 34 : 27

# 답 2
# 구분자 sep를 사용해서 분리해 출력
print(year, month, day, sep="/", end = " " )
print(hour, minute, second, sep = ":")
# 2019/04/26 11:34:27
