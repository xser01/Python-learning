def zfc_definition(n: int) -> str:#我的错误代码
    last=[]
    now=[]
    for _ in range(n):
        now.append(last)
        last=now
    now=str(now)
    a=now.replace('[','{')
    a=a.replace(']','}')
    return a
def zfc_definition(n):#正确代码
    if n == 0:
        return "{}"
    return "{" + ",".join(zfc_definition(i) for i in range(n)) + "}"
#多个赋值，顺序结构赋值，赋值问题赋予谁，需要看流程变化
#在函数内调用本函数－>指的是递归
'''def function(参数):
    if 结束条件:
        return 结果
    function(更小的问题)
'''
#在if条件中，if指的是基准情况或者是结束条件；而在function中，指的是更小的问题，并且向结束条件靠近
#（主要2）我把当前问题变成一个更小的同类问题，然后让同一个函数继续解决。
#(主要1)，进入子问题以后，做的事情和原来的事情完全一样。