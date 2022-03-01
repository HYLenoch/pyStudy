# int()函数用于 将其他进制的字符串转10进制的使用
# 反过来可用hex、oct、bin将10进制数转成对应进制的字符串

num = int('1010', base=2)
print(num)

print('--------------')

num = int('-654321', base=7)
print(num)

print('--------------')

num = int(hex(32), base=16)
print(num)

