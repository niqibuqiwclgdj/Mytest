'''def funNum(a):
    i = 0
    s = ""
    a = str(a)
    print("原形参：" + a)
    j = len(a) - 1
    while i<len(a):
        s += a[j]
        j -=1
        i +=1
    return s
print("改变后：" + funNum("WOMEN"))'''

number=input().split()[0]
output=''
for i in range(len(number)-1,-1,-1):
    output+=number[i]
print(output)