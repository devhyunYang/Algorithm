# 리스트에서 2와 3를 삭제해라

a = [1, 2, 3, 4, 5, 6]


# 오답 1 : remove는 1개의 argument만 가능
a.remove(2, 3)

# 정답 1
a.remove(2)
a.remove(3)

# 정답 2
del a[2:3]
