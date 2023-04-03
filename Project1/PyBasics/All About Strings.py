# xxx开头
v1 = 'Today is a good day'
result = v1.startswith('Today')
print(result)

# example

v1 = 'Beijinger'
if v1.startswith('Beijing'):
    print('Beijinger')
else:
    print('non Beijinger')

# xxx 结尾
address = 'srthsrth'
if address.endswith('village'):
    print('villager')
else:
    print('non vilager')

# 是否为整数
v3 = '12385'
result = v1.isdecimal()

# 去除字符串两边的空格、换行符、制表符、得到一个新的字符串
msg = ' Hell o e d  d i e    '
data = msg.strip().lstrip().rstrip()
print(data)

# 大小写
a = msg.upper().lower()

# 内容替换

v4 = v3.replace('123', '555')
print(v4)

char_list = ['fuck', 'shit', 'bitch']
content = 'fuck this shit that cunt cock asshole'
for item in char_list:
    content = content.replace(item, '***')
print(content)

# 字符串切割，得到一个列表

data = 'aergioj.adfv.fgb.aarg.hsrt.a.dafv.'
result = data.split('.')
result2 = data.split('.',1) #从第一个开始切割 后面为整体
print(result)

result3 = data.rsplit('.', 1)
print(result2)
print(result3)

# 字符串拼接，得到新字符串
data_list = ['eddie', 'is', 'man']
v5 = ' '.join(data_list)
print(v5)

#字符串转换为字节类型
data = '李昌昊'
v1 = data.encode('utf-8')
v2 = data.encode('gbk')

print(v1)
print(v2)

print(v1.decode('utf-8'))

# 居中、居左、居右
data = '李'
print(data.center(21,'-'))
print(data.ljust(21,'-'))
print(data.rjust(21,'-'))

# 帮助填充0(处理二进制数据）

data = '101'
print(data.zfill(8))

#  str + str
v1 = 'da+va'

# str * 3
data = 'ed' *3
print(data)

# 字符串长度
print(len(v1))

# 截取str
message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(message[0:2])
print(message[3:7])
print(message[3:])
print(message[:5])
print(message[4:len(message)])
print(message[:-2])
print(message[0:len(message):2]) #调一个取值
print(message[::-1])