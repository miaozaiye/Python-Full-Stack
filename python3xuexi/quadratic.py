
import cmath
import math
import sys


# 循环直至用户输入一个有效浮点数
def get_float(msg,allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x)<sys.float_info.epsilon:
                print('zero is not allowed')
                x = None
        except ValueError as err:
            print (err)
    return x

#获取用户输入有效浮点数 a,b,c
print('ax\N{SUPERSCRIPT TWO}+bx+c=0')
a = get_float("enter a:",False)
b = get_float("enter b:",True)
c = get_float("enter c:",True)

#计算 X
x1 = None
x2 = None
D = (b**2)-(4*a*c)
if D == 0:
    x1 = -(b/2*a)
else:
    if D > 0:  #如果判定式大于0，则为实数解
        root = math.sqrt(D)
    else: #如果判定式小于0，则为虚数解
        root = cmath.sqrt(D)
    x1 = (-b+root)/(2*a)
    x2 = (-b-root)/(2*a)


join1 = '+' if b >=0 else ''
join2 = '+' if c >=0 else ''


equation = ("{0}x\N{SUPERSCRIPT TWO}"+join1+"{1}x"+join2+"{2}=0\N{RIGHTWARDS ARROW}x = {3}").format(a,b,c,x1)


# 逐字寻找，发现"+"／"-"号之后直接是"0"，则对字符串切片，【：加减号位置】+【加减号位置：】
lo = equation.find('0.0')  #s.find(str), 返回str在字符串中最左的位置，如果没有，则返回-1
while lo!=-1:
    if equation[lo+3]=='x':
        equation = equation[:lo-1]+equation[lo+4:]
        lo = equation.find('0.0')
    else:
        equation = equation[:lo-1]+equation[lo+3:]
        lo = -1



if x2 is not None:
    equation += " or x = {0}".format(x2)
print (equation)
