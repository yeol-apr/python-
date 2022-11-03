def mappao(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                b = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = b
    return arr


list = []
while True:
    a = int(input('请输入需要排序的数，999结束'))
    if a != 999:
        list.append(a)
    else:
        break;
lists = mappao(list)
for listes in lists:
    print(listes, end=" ")
