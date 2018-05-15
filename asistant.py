from os import system
from time import sleep
import webbrowser 
import os 
import subprocess

urls =  ["https://www.youtube.com","https://www.facebook.com","https://ww5.gogoanime.io/popular.html",
"https://www.watchcartoononline.com","https://stackoverflow.com/"]
#screen clear function
def cls():
	system('cls')
	
#chill mode function
def chill_mode():
	webbrowser.open_new_tab(urls[0])
	webbrowser.open(urls[1])
	webbrowser.open(urls[2])
	webbrowser.open(urls[3])
#text space function
def space():
	print("")


#close cmd function

def close_prompt():
	system("TASKKILL /f /im cmd.exe")

#study mode function 

def study_mode():
	os.startfile("C:/Users/holden/Downloads/48 laws of power.pdf")
	os.startfile("C:/Users/holden/Downloads/Rich Dad Poor Dad.pdf")
	os.startfile("C:/Users/holden/Desktop/movies/CCNA ICND1 100-105")
	
	system("TASKKILL /f /im chrome.exe")

def program_mode():
	system("TASKKILL /f /im chrome.exe")

	sleep(2)
	
	webbrowser.open(urls[4])
	webbrowser.open(urls[0])
	os.startfile("C:/Program Files (x86)/Geany/bin/geany.exe")
	os.startfile("C:/Users/holden/Desktop/python")
#intro 

print("Holden's asistant")

sleep(2)

cls()
#print modes 

print("Pick a Mode: ")
space()

sleep(0.5)

print("1. Chill Mode")

print("2. Study Mode")

print("3. Program Mode")

space()
#users pick 

Pick=input(": ")

if Pick == str(1):
	chill_mode()
	cls()
	close_prompt()
	
elif Pick == str(2):
	study_mode()	
	close_prompt()
	
elif Pick == str(3):
	program_mode()
	close_prompt()	
	
else:
	print("error")	
	
	

