a=['1','2','3','4','5','6','7','8','9']

def print_board():
	print(a[0],'|',a[1],'|',a[2])
	print("-------")
	print(a[3],'|',a[4],'|',a[5])
	print("-------")
	print(a[6],'|',a[7],'|',a[8])
	print("-------")

playeroneturn = True
while True:
	print_board()
	p=input("choose the place: ")


	if(p in a):
		if(a[int(p)-1]=='x' or a[int(p)-1]=='o'):
			print("place taken,choose another place..")
			continue

		else:
			if playeroneturn:
				a[int(p)-1]='x'
				playeroneturn = not playeroneturn
			else:
				a[int(p)-1]='o'
				playeroneturn = not playeroneturn
			for i in(0,3,6,):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("game over")
					exit()
			for i in range (3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("game over")
					exit()




		



