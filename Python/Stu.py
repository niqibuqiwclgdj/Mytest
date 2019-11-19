name = ["jidao" ,"jirui" , "ji" , "xdd" , "rui"]
print("这是原来的列表：")
print(name)
print("-"*50 + "\n")

print("这是append操作的列表：")
name.append("jidao")
print(name)
print("-"*50 + "\n")

print("这是insert操作的列表")
name.insert(0 , "jidao")
print(name)
print("-"*50 + "\n")

print("这是del操作的列表")
del(name[0])
print(name)
print("-"*50 + "\n")

print("这是remove操作的列表")
name.remove("jidao")
print(name)
print("-"*50 + "\n")

print("这是pop操作的列表")
name.pop(1)
print(name)
print("-"*50 + "\n")

print("这是sort操作的列表")
name.sort(reverse = False)
print("降序排序：" + str(name))
name.sort(reverse = True)
print("升序排序：" + str(name))
print("-"*50 + "\n")
