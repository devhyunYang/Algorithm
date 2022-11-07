# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

# 오답 1
A = int(input())
B = int(input())

Answer = A - B

# 정답
A, B = input().split()
A = int(input())
B = int(input())

print(A-B)