"""
练习：在终端中输入一个四位整数，计算每位相加和。
例如：录入1234，打印1+2+3+4结果
效果：
请输入四位整数：1234
结果是：10
"""

num = int(input("请输入四位整数："))

# ge = num % 10
# shi = num // 10 % 10
# bai = num // 10 // 10 % 10
# qian = num // 10 // 10 // 10
#
# result = ge + shi + bai + qian

# 优化
result = num % 10
temp = num // 10
while True:
    if temp < 10:
        result += temp
        break
    result += temp % 10
    temp //= 10


print(f"结果是：{result}")
