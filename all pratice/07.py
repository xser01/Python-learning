#1
def solve(n):#我的代码
    f1,f2='0','01'
    if n==0:
        return f1
    elif n==1:
        return f2
    else:
        count1=1
        while count1<n:
            count1+=1
            f1,f2=f2,f2+f1
        return f2
            
    pass
def solve(n):#参考代码
    a,b = '01'
    for _ in range(n): a,b = a+b,a
    return a
#这里用到了更新，a,b=b,a+b，以a替代原本的b，b作为结果形成一个新的值，让a、b、a＋b整体后移
#这里最重要的是状态值，更新的是状态，而不是将每一个值都具体保留
#对于for _ in range()中的‘_’，表示游历但是不使用，而range（）表示范围
#事实上，while也可以表示，只不过while更强调什么时候结束，而for _ in 范围，更加强调范围，从哪里游历循环到那里
#2
def solution(text, ending):
    # your code here...
    return text.endswith(ending)
    pass
#单纯Python内置函数.endswith()的使用
#3
def letter_check(string_pair: list[str]) -> bool: 
    # your code here
    ob1=set(string_pair[1].lower())
    ob2=set(string_pair[0].lower())
    return ob1<=ob2
#查找使用set更快，这里是集合的运算，‘＆‘，’set1.isdisjoint(set2),->.isdisjoint(object)指的是判断两个对象有没有公共元素‘