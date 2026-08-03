#1。isinstance()函数的使用
def filter_list(l):
    rezults=[]
    for num,word in enumerate(l):
        if isinstance(word,int)==True and word>=0:
            rezults.append(word)
        else:
            continue
    return rezults

#2.有关于切片的提高
def partlist(arr):
    rezults=[]
    for num in range(1,len(arr)):
        list_repeat=()
        one=" ".join(arr[:num])
        two=" ".join(arr[num:])
        list_repeat=(one,two)
        rezults.append(list_repeat)
    return rezults
    # your code