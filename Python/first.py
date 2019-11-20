school = {"zhouan":[100 , 90 , 111 , 120] , "wulaodi":[99 , 99 , 99 , 99] , "jidao":[11 , 112 , 123 , 134]}
for name , grades in school.items():
	print(name + "的语文为：" + str(grades[0]))
	print(name + "的数学为：" + str(grades[1]))
	print(name + "的英语为：" + str(grades[2]))
	print(name + "的编程为：" + str(grades[3]))
		