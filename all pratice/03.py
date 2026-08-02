#题目1，代码2、3为示范代码
def calculate_age(year_of_birth, current_year):
    a=year_of_birth
    b=current_year
    num=b-a
    if num>0:
        if num==1:
            return f"You are {num} year old."
        else:
            return f"You are {num} years old."
    elif num<0:
        if num==-1:
            return f"You will be born in {-num} year."
        else:
            return f"You will be born in {-num} years."
    else:
        return f"You were born this very year!"
    pass


def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    plural = '' if diff == 1 else 's'
    if year_of_birth < current_year:
        return 'You are {} year{} old.'.format(diff, plural)
    elif year_of_birth > current_year:
        return 'You will be born in {} year{}.'.format(diff, plural)
    return 'You were born this very year!'


def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 0:
       return "You were born this very year!"
    elif age > 0:
       return "You are {} year{} old.".format(age, 's' if age > 1 else '')
    else:
       return "You will be born in {} year{}.".format(abs(age), 's' if abs(age


#题目2，2、3为示范代码
def polygon_area(a, b, c, d):
    return a*b+b*(c-a)*0.5
    passdef calculate_age(year_of_birth, current_year):
    a=year_of_birth
    b=current_year
    num=b-a
    if num>0:
        if num==1:
            return f"You are {num} year old."
        else:
            return f"You are {num} years old."
    elif num<0:
        if num==-1:
            return f"You will be born in {-num} year."
        else:
            return f"You will be born in {-num} years."
    else:
        return f"You were born this very year!"
    pass


def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    plural = '' if diff == 1 else 's'
    if year_of_birth < current_year:
        return 'You are {} year{} old.'.format(diff, plural)
    elif year_of_birth > current_year:
        return 'You will be born in {} year{}.'.format(diff, plural)
    return 'You were born this very year!'


def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 0:
       return "You were born this very year!"
    elif age > 0:
       return "You are {} year{} old.".format(age, 's' if age > 1 else '')
    else:
       return "You will be born in {} year{}.".format(abs(age), 's' if abs(age))


#题目3，优化
def polygon_area(a, b, c, d):
    if b!=0 and a!=0 and c!=0 and d!=0:
        return a*b+0.5*b*(c-a)
    elif b==0 or d==0:
        return 0
    elif a==0 and c==0:
        return 0
    elif a==0:
        return 0.5*(d+b)*c-0.5*d*(c-a)
    elif c==0:
        return a*b+0.5*b*(c-a)-a*0.5*d
    pass

def polygon_area(a, b, c, d):
    return a*b+b*(c-a)*0.5
    pass