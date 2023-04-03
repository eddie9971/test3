# 1. 循环提示用户输入内容（q终止），并用‘——’连接起来 --------------------------------------------------------------------------
# data_list = []
# while True:
#     text = input('type')
#     if text.lower() == 'q':
#         break
#     data_list.append(text)
#
# result = '_'.join(data_list)
# print(result)
#

# 2. 将IP地址转换为整数，并拼接 --------------------------------------------------------------------------
ip = '117.135.84.76'

data_list = []
num_list = ip.split('.')
for num in num_list:
    n = bin(int(num))[2:].zfill(8) #2: 去除前面二进制的表示字母，去除后不满8位，zfill填充
    data_list.append(n)

reverse_data = ''.join(data_list)[::-1]
result = int(reverse_data,base =2)
# print(result)

# 3. 车牌区域划分，获取各省车牌数量 --------------------------------------------------------------------------
car_list = ['京03945', '津09238','沪123123','京03945', '津09238','沪123123',]
info = {}
for i in car_list:
    city = i[0]
    if city in info:
        info[city] = info[city]+1
    else:
        info[city] = 1

# print(info)

info2 = {}
for i in car_list:
    city = i[0]
    num = info.get(city, 0) #get city这个key的值，如果存在就取目前的值，如果不存在就设置为0
    info[city] = num + 1
# print(info2)

# 4. 数据格式化处理 --------------------------------------------------------------------------
text = '''
id,name,age,phone,job
1,alex,22,123123,IT
2,Jack,23,123123,Teacher
3,Oliva,24,123123,IT'''

data_list = text.split('\n')
del data_list[0]
header_list = data_list[0].split(',')
info = []
for index in range(1,len(data_list)):
    item = {}
    row = data_list[index]
    row_item_list = row.split(',')
    for i in range(len(row_item_list)):
        item[header_list[i]] = row_item_list[i]
    info.append(item)
print(item)

# 5.题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？--------------------------------------------------------------------------
# for i in range(1,5):
#     for e in range (1,5):
#         for a in range (1,5):
#             if i != e and i != a and e != a:
#                 print(i,e,a, sep='')

# 6.题目：企业发放的奖金根据利润提成。利润 (I)  低于或等于10万元时，奖金可提10%；利润高于 -------------------------------------------
# 10 万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成 7.5%；20万到 40 万之间时，高于20万元的部分，可提成
# 5%；40万到60万之间时高于 40万元的部分，可提成 3%；60万到100 万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过 100
# 万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# i = int(input('Enter Total Revenue: '))
# array = [1000000, 600000, 400000, 200000, 100000, 0]
# rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# bonus = 0
# for idx in range (0,6):
#     if i > array[idx]:
#         bonus +=(i-array[idx])*rate[idx]
#         print((i-array[idx])*rate[idx])
#         i=array[idx]
# print(bonus)

# 7.输入某年某月某日，判断这一天是这一年的第几天？ --------------------------------------------------------------------------
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需要考虑多加一天

# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
#
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0 < month <= 12:
#     sum = months[month-1]
# else:
#     print('data error')
# sum += day
#
# leap = 0
# if (year % 400 == 0) or ((year % 4 ==0) and (year % 100 !=0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print(f'it is the {sum} day')


# 8.输入三个整数x,y,z, 从小大大排列 --------------------------------------------------------------------------
#
# number = []
# for i in range (3):
#     x = int(input('Integer:\n'))
#     number.append(x)
# number.sort()
# print(number)

# 9.Fibonacci sequence --------------------------------------------------------------------------
# def fibonacci_of(n):
#     if n==1 or n ==2:
#         return 1
#     return fibonacci_of(n-1) + fibonacci_of(n-2)
#
# print(fibonacci_of(9))

# 10.9*9乘法表 --------------------------------------------------------------------------
# for i in range (1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i} = {j*i}', end=' ')
#     print()

# 输入一行字符，分别统计出来其中英文字母、空格、数字、和其他字符的个数

# import string
# s = input('Enter a sentence:\n')
# letters = 0
# space = 0
# digit = 0
# others = 0
#
# for e in s:
#     if e.isalpha():
#         letters += 1
#     elif e.isspace():
#         space += 1
#     elif e.isdigit():
#         digit += 1
#     else:
#         others += 1
# print(f'Char:{letters}, space:{space}, digit:{digit}, others:{others}')

# 输入一行字符，分别统计出来其中英文字母、空格、数字、和其他字符的个数

# import string
# s = input('Enter a sentence:\n')
# letters = 0
# space = 0
# digit = 0
# others = 0
#
# for e in s:
#     if e.isalpha():
#         letters += 1
#     elif e.isspace():
#         space += 1
#     elif e.isdigit():
#         digit += 1
#     else:
#         others += 1
# print(f'Char:{letters}, space:{space}, digit:{digit}, others:{others}')