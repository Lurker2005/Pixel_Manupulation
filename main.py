from PIL import Image

def enc(inp,k):
	pixelmap=inp.load()
	wid,hei=inp.size
	
	for i in range(wid):
		for j in range(hei):
			r,g,b=inp.getpixel((i,j))
			r=r^k
			g=g^k
			b=b^k
			pixelmap[i,j]=(r,g,b)
			
	inp.save("encyrpterd",format="png")
	print("the image encryption is completed")
def dec(inp,k):
	pixelmap=inp.load()
	wid,hei=inp.size
	
	for i in range(wid):
		for j in range(hei):
			r,g,b=inp.getpixel((i,j))
			r=r^k
			g=g^k
			b=b^k
			pixelmap[i,j]=(r,g,b)
			
	inp.save("decrypted",format="png")
	print("the image decryption is completed")
while(True):
	print("1.encrypt")
	print("2.decrypt")
	print("3.exit")
	c=int(input("Enter your choice: "))
	if(c==1):
		inpu=input("enter the inputfile name : ")
		inp=Image.open(inpu)
		k=int(input("enter the key: "))
		enc(inp,k)
	elif(c==2):
		inpu=input("enter the inputfile name : ")
		inp=Image.open(inpu)
		k=int(input("enter the key: "))
		dec(inp,k)
	elif(c==3):
		print("Exiting....")
		break
	else:
		print("enter the corect choise")
