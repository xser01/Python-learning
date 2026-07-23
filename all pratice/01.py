'''#题目：输入一个数字，并把这一个数字的每一位数换成平方并合并起来输出
def square_digits(num):
    num=int(num)                    #这里使用的是数学的计算的代码，事实上使用字符串的方法要快很多
if num<10:                           #使用Python编写代码时,经可能的结合Python本身的特性
        return num**2
    else:
        count01=len(str(num))
        shuchu=""
        for number in range(1,len(str(num))+1):
            count01-=1
            if num>10:
                shuwei=num//10**count01
                num-=shuwei*10**count01
                shuchu=shuchu+str(shuwei**2)
            else:
                shuchu=shuchu+str(num**2)
                return int(shuchu)
# Your code here
num=input("number")
print(square_digits(num))'''


'''def square_digits(num):
    # 1. 强制转换为字符串（无论传进来的是 int 还是 str 都能处理）
    str_num = str(num)
    
    # 2. 定义一个空字符串用来存放拼接结果
    result = ""
    
    # 3. 遍历字符串中的每一个数字字符
    for char in str_num:
        digit = int(char)       # 转回整数
        sq_digit = digit ** 2   # 计算平方
        result += str(sq_digit) # 转成字符串追加到结果中
        
    # 4. 返回最终转成的整数结果
    return int(result)

# 测试运行
num = input("请输入数字: ")
print(square_digits(num))
'''