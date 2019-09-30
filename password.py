password = 'a12'
i = 3 #剩餘機會
i = i - 1
while i > 0 :
	pwd = input('please enter the password')
	if pwd == password :
		print('log in  successfully')
		break # 逃出迴圈
	else : 
		print('pwd is wrong')
		if i > 0 :
			print('you still have ',i,'opportunities')
		else :
			print('no opportunity , your account is blocked')