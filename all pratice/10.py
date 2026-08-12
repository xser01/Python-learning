def sort_dict(d):
    list_tuple=[]
    for key,value in d.items():
        list_tuple.append((key,value))
    return sorted(list_tuple,key=lambda x:x[1],reverse=True)
def sort_dict(d):
    return sorted(d.items(),key=lambda x:x[1],reverse=True)
#对于key函数，key＝函数，key后必须接函数
#lambda函数，格式为lambda x：x【0】，第一个x为接收进去的数据，x【0】为实际从lambda函数输出到外部的内容
#dict数据类型中的items（）方法，返回的是一个【（a：b），（c：s）】的东西，本质还是dict类型
#需要将其转为list类型才能使用list方法，但items后可以游历操作的，因为它本质还是一个iterable，可迭代对象。
'''
dict_items([
    ("a", 3),
    ("b", 1),
    ("c", 5)
])
'''#对于items，得到的是一个dict_items对象，字典视图对象，如上