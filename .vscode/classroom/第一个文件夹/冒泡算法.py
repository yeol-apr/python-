def mappao(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                b=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=b
    return arr

list=[1,2,5,3,6,9]
lists=mappao(list)
for listes in lists:
    print(listes)
