"""
练习：在终端中输入商品单价、购买的数量和支付金额。计算应该找回多少钱。
效果：
请输入商品单价：5
请输入购买数量：3
请输入支付金额：20
应找回：5.0
"""

single = float(input("请输入商品单价："))
number = float(input("请输入购买数量："))
money = float(input("请输入支付金额："))
charge = money - single * number
print(f"应找回：{charge}")