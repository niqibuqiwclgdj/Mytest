name = ["zhouan" , "jidao" , "afei" , "xiaolu" , "wuxiaolaodi" , "xulaodi"]
print("这是原始列表：")
print(name)
print("------------------------")

print("这是append操作的列表：")
a = name.append("xdd")
print(name)
print("-------------------------")

print("这是insert操作的列表：")
b =name.insert(0 , "zhouan")
print(name)
print("--------------------------")

print("这是del操作的列表：")
del(name[0])
print(name)
print("--------------------------")

print("这是pop操作的列表：")
name.pop(-1)
print(name)
print("--------------------------")

print("这是remove操作的列表：")
c = name.remove("zhouan")
print(name)
print("--------------------------")

print("这是经历过一系列操作的后列表：")
print(name)
