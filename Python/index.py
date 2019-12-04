'''def func(s):
    result = ""
    len_index = len(s)-1
    for index,value in enumerate(s):
        result += s[len_index-index]
    return result

s = input("输入你想要进行转换的文本: ")
res = func(s)
print("反转后的结果为: " + res)'''

def change(a):
    a = a[::-1]  #切片操作
    return a
a = input("输入你想要反转的文本: ")
res = change(a)
print("这里是反转后的文本: " + res)