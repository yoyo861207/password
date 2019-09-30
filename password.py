password = 'a12'
i = 3 #剩餘機會
while True :
	pwd = input('please enter the password')
	if pwd == password :
		print('log in  successfully')
		break # 逃出迴圈
	else : 
		i = i - 1
		print('pwd error! you still have ',i,'opportunities') 
		if i == 0 :
			break