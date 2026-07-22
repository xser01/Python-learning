def multiple_of_index(arr):
    list_chuncu=[]
    shuru=arr
    list_yuan=list(shuru)
    for arr_1 in shuru:
        num=list_yuan.index(arr_1)
        if  num == 0:
            continue
        else:
            if int(arr_1)%num==0:
                list_chuncu.append(arr_1)
    return list_chuncu
a=input("aaa")
b=multiple_of_index(a)
print(b)


import json                                 #用到了json，是处理字符串的的库
def multiple_of_index(arr):
    list_chuncu = []
    # 从 1 开始遍历下标，直接避开 0
    for num in range(1, len(arr)):
        arr_1 = arr[num]
        if int(arr_1) % num == 0:
            list_chuncu.append(arr_1)
    return list_chuncu

# 处理输入：将输入的字符串转换为实际的 Python 列表
a = json.loads(input("请输入列表（例如 [1, 3, 44, 55])"))
b = multiple_of_index(a)
print(b)
