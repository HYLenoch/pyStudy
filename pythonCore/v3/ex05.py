"""
让下列代码重复执行，输入y继续(不输入y则退出)
"""

while True:
    month = input('请输入月份1-12：')
    if '1' == month or '3' == month or '5' == month or '7' == month or '8' == month or '10' == month or '12' == month:
        print(f'{month}月有31天。')
    elif '4' == month or '6' == month or '9' == month or '11' == month:
        print(f'{month}月有30天。')
    elif '2' == month:
        print(f'{month}月有29天。')
    else:
        print('您输入的月份有误。')
    if input("输入y继续，否则退出,请输入：") != 'y' :
        break;