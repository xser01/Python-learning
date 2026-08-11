def is_uppercase(inp):
    import string
    lower_set=set(string.ascii_lowercase)
    return set(inp).isdisjoint(lower_set)
#string库，isdisjoint（）方法－>判断是否没有任何子集
def no_space(x):
    rezults=''
    for word in x:
        if word!=' ':
            rezults+=word
    return rezults
    #your code here
def no_space(x):
    return x.replace(' ','')
    #your code here
#这里使用了replace（）方法，将对象中所有的元素替换为另一个元素
def contamination(text, char):
    text1=text
    for w in text:
        if w!=char:
            text1=text1.replace(w,char)
    return text1
#同上
def string_to_array(s):
    list1=list(s.split(" "))
    return list1
    # your code here
#对于字符串中，s＝‘app‘，若是使用list（s），print，则输出【’a‘，’p‘，’p‘】每一个字母按元素加如list数据类型