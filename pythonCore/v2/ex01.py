"""
    人民币转美元 汇率转换
"""

# 1. 获取人民币
cny = float(input("请输入人民币："))
# 2. 逻辑计算
usd = cny * 0.16
# 3. 显示结果：xx人民币 = yy 美元
print(str(cny) + "人民币 = "+ str(usd)+"美元")
