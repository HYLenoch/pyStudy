"""
在终端中输入课程阶段数,显示课程名称
效果：
输入： 输出：
 1      Python语言核心编程
 2      Python高级软件技术
 3      Web 全栈
 4      项目实战
 5      数据分析、人工智能
"""

choice = int(input("请输入数字1-5："))

if choice == 1:
    print('Python语言核心编程')
elif choice == 2:
    print('Python高级软件技术')
elif choice == 3:
    print('Web 全栈')
elif choice == 4:
    print('项目实战')
elif choice == 5:
    print('数据分析、人工智能')