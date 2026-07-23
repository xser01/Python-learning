'''def multiple_of_index(arr):
    import json
    files=json.loads(arr)
    list01=[]
    for i in range(1,len(files)):
        if int(files[i])%i==0:
            list01.append(files[i])
        else:
            continue
    print(list01)
arr=input("a")
multiple_of_index(arr)

#可运行的代码'''

"""def multiple_of_index(arr):
    import json
    files=json.loads(arr)
    list01=[]
    for i in range(1,len(files)):
        if int(files[i])%i==0:
            list01.append(files[i])
        else:
            continue
    return list01
    pass
    
#codewar上正确的代码"""

"""import json                                 #用到了json,是处理字符串的的库
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
print(b)"""
