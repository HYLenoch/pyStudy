# 查看python保留字

import keyword

kwlist = keyword.kwlist
print(kwlist)

for i in range(len(kwlist)):
    if i % 4 == 0:
        print()
    print("%-15s" % kwlist[i], end="")
