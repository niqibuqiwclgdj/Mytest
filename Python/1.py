i = 1
a = []
while i < 11:
    num = int(input("请输入第" + str(i) + "个数字："))
    i +=1
    if num%2 != 0:
        a.append(num)
print(a)