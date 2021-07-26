import time
import random
from os import system
system('clear')
print ("Welcome to Hogwarts School of Witchcraft and Wizardry Online House Chooser")
time.sleep(1)
print ("""
During this troubling time, Hogwarts School of Witchcraft and Wizardry has decided to move to a fully online system. More
information can be found of this matter at hogwarts.co.uk
Thank you for your understanding of the struggle to continue schooling online.
All the best,
Albus Dumbledore

P.S. Be aware, Voldemort has hacked our website. Do not accept any unidentified online payments using our website because somehow Voldemort can use PayPal. Our research says he may be dictating another being to create his PayPal transactions.
"""
)
input ("Press enter when you have fully read and understood this message...")
system('clear')

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

print ("It is now time to create your Hogwarts account.")
firstname = input ("Please type in your first name: ")
lastname = input ("Please type in your surname: ")
account = firstname+"."+lastname+"@hogwarts.co.uk"
print (f"Your Hogwarts username is {account}. Please remember this username otherwise you will be locked out of your account.")
system('clear')

accountattempt = ""
while accountattempt != account:
	accountattempt = input ("Please type in your hogwarts username: ")

print ("You have sucessfully logged in to your hogwarts account.")
input("Press enter when you would like to start house picker...")
print ("Loading...")
time.sleep(20)
randomnumber = random.randint(40,50)
counter = 0
house = ""
for r in range(randomnumber):
	house = houses[counter]
	print (house)
	counter = counter+1
	if counter > 3:
		counter = 0
	time.sleep(0.3)
	system('clear')
print (f"Yay! Your house is {house}.")
input("Press enter when you are ready to exit...")