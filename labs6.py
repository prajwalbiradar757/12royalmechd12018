import random
count=0
def myroll():
	return random.randint(1,6)

while(count<=100):
	n=input("press r roll the dice")
	if(n=='r'):
		r=myroll()
		count=count+r
		print("u got",r)
		print("new position is",count)

		if(count==8):
			count=37
			print("i got the ladder")
		elif(count==11):
			count=2
			print("sorry,u got snake")
		elif(count==3):
			count=34
			print("i got the ladder")
		elif(count==38):
			count=9
			print("sorry,u got snake")
		elif(count==40):
			count=68
			print("i got the ladder")
		elif(count==65):
			count=46
			print("sorry,u got snake")
		elif(count==52):
			count=81
			print("i got the ladder")
		elif(count==89):
			count=70
			print("sorry,u got snake")
		elif(count==76):
			count=97
			print("i got the ladder")
		elif(count==93):
			count=64
			print("sorry,u got snake")
		if count==100:
			print("u r winner")
			break
		if count>100:
			print("u cannot move")
			count=count-r