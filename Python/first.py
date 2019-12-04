thing = {"aaa":[60 , 66 , 86 , 69] , "bbb":[76 , 66 , 96 , 80] , "ccc":[69 , 65 , 97 , 96]}
for name , results in thing.items():
	print(name + "的python成绩为：" + str(results[0]))
	print(name + "的java成绩为：" + str(results[1]))
	print(name + "的JavaWeb成绩为：" + str(results[2]))
	print(name + "的C语言成绩为" + str(results[3]))
	print("-"* 40)
