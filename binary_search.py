x = 3

a = [1, 2, 3, 4, 10, 0]
a.sort()

left = -1
right = len(a) - 1

while left < (right - 1):

    mid = (left + right) // 2

    if a[mid] > x:
        right = mid
    else:
        left = mid

if left >= 0 and a[left] == x:
    print(x)
else:
    print(-1)
