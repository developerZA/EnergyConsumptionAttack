# Connecting to mysql database
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
 
 
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="meter")
mycursor = mydb.cursor()
 


mycursor.execute("select watt, idd from powerar1 where watt between 0.212 and 0.245")
result = mycursor.fetchall
 
Watt = []
Hours = []
 
for i in mycursor:
    Watt.append(i[0])
    Hours.append(i[1])

mycursor.execute("select watt, idd from powerar2 where watt > 0.245")
result = mycursor.fetchall
 
Watt1 = []
Hours1 = []
 
for i in mycursor:
    Watt1.append(i[0])
    Hours1.append(i[1])


mycursor.execute("select watt, idd from powerar3")
result = mycursor.fetchall
 
Watt11 = []
Hours11 = []
 
for i in mycursor:
    Watt11.append(i[0])
    Hours11.append(i[1])


mycursor.execute("select watt, idd from powerar4")
result = mycursor.fetchall
 
Watt111 = []
Hours111 = []
 
for i in mycursor:
    Watt111.append(i[0])
    Hours111.append(i[1])
 



plt.ylabel("Energy Consumption (A)")
plt.xlabel("Time (S)")
plt.title("Arduino Power Consumption")
#plt.plot(Hours, Watt, label = "before attack")
plt.plot(Hours, Watt, 'tab:blue')
plt.plot(Hours1, Watt1, 'tab:red')
plt.plot(Hours11, Watt11, 'tab:green')
plt.plot(Hours111, Watt111, 'tab:orange')
#plt.legend();
plt.show()
