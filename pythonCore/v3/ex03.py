"""
在终端中输入月份，打印相应的天数.
1 3 5 7 8 10 12 有 31天
2 有 29天
4 6 9 11 有 30天
超过月份提示月份有误
效果：
请输入月份:10
31天

"""
month = input('请输入月份1-12：')
if '1' == month or '3' == month or '5' == month or '7' == month or '8' == month or '10' == month or '12' == month:
    print(f'{month}月有31天。')
elif '4' == month or '6' == month or '9' == month or '11' == month:
    print(f'{month}月有30天。')
elif '2' == month:
    print(f'{month}月有29天。')
else:
    print('您输入的月份有误。')