'''def is_isogram(string):
    keeping=""
    for word1 in string:
        keeping+=word1                      #没有必要再放入且循环一次，直接检查单词有没有重复单词就已经可以了
        for word2 in string:
            if keeping.count(word2)==2:
                return "false"
            else:                           #这里提前结束了循环无论是什么条件下，他都会终止代码
                return "true"#your code here'''


'''def is_isogram(string):
    string=string.lower()         #注意要将大小写转换
    for word in string:
        a=string.count(word)
        if a>1:
            return False
    return True#your code here'''


'''def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))＃这里直接使用的了集合去重的性质，利用了Python的特性，更简洁更直接，时间更快'''