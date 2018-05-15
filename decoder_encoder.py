import codecs 
import time 
import os

def encoder():
	Input = input("encode data: ")
	coder= codecs.encode(Input,'rot13')
	
	if Input == "-b":
		pickmode()
	print("")
	print(coder)
	
def decoder():
	Input = input("decode data: ")
	coder = codecs.decode(Input, 'rot13')
	
	if Input == '-b':
		pickmode()
	print("")
	print(coder)
	
def pickmode():
	Input =input("Pick a mode: ")
	
	if Input == "-e":
		encoder()
	elif Input == "-d":
		decoder()
	elif Input == 'Exit':
		running = False 
		quit()
	else:
		print("")
		print("Not a valid command")		
	
	
def intro():
	print("Use -e to enter encode mode")
	time.sleep(2)
	print("Use -d to enter decode mode")	
	time.sleep(2)
	print("Use -b to go back to mode selection")
	time.sleep(2)
	os.system('cls')
						
running = True 

while running:
	intro()
	pickmode()
	
	running = False 	
				
