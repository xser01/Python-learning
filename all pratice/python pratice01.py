import json
def reverse_01(s):
    list_z=[]
    s=json.loads(s)                     
    nums=len(s)
    for num in range(1,nums+1):    #不要将所有的检索完才去去重，在检索过程中就直接加入到列表中
        for object in s:
            object=int(object)
            k=object/num
            if k.is_integer():
                list_z.append(object)
    list_a=[]
    for i in list_z:             #这里用到了去重，但实际上十分低效，因为在前面的循环中，做了
        if i not in list_a:      #大量无意义的循环，应当在成功检索到正确的数字之后就停止游历
            list_a.append(i)
    print(list_a)
s=input("numbers")
reverse_01(s)


import json
def filter_multiples(s):
    s = json.loads(s)
    n = len(s)
    result = []
# 外层循环：逐个检查输入列表中的每一个数zi
#for object in s:
    object = int(object)# 内层循环：检查这个数字能否被 1 到 n 之间的任意一个数整除
    # 注意：这里用 n + 1 才能包含数字 n 本身
    for num in range(1, n + 1):
        if object % num == 0:     # 使用 % 取余判断整除更高效地道
            result.append(object) # 只要能被其中一个整除，就录用                   
            break                 # 绝杀：立刻跳出内层循环，防止同一个数字被重复添加！
    print(result) # 测试
    s = input("numbers: ") # 比如输入 [1, 3, 44, 55]
    filter_multiples(s)                                                                        