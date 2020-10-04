lista = [
    [1,1,1,0,2,1,0,0,2,0,1,0],
[1,1,1,0,2,1,0,0,2,0,0,0,1],
[0,2,2,2,0,0,0,1,2,1,1,0,0,0],
[3,3,3,3,3,3,3,1,0,0,0,1]

]

for listita in lista:
	print('///////')
	primero = True
	cantidad = 0
	index = 0
	while ( index <= len(listita)-1 ):
		
		if(primero):	
			index = index + listita[index]+ 1
			primero = False	
		

		else:

			if(listita[index]==0):
				index = index + 1

			elif (listita[index]==1):
				index = index + 2

					
			elif(listita[index]==2):
				index = index + 3

					
			elif (listita[index]==3):
				index = index + 4

		cantidad = cantidad+1
	
	
	print("Minima cantidad de regadera es ")
	print(cantidad)

