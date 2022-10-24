# Connecting to mysql database
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
 
 
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="meter")
mycursor = mydb.cursor()
 


mycursor.execute("select wat, idd from power11 where watt between 0.282 and 0.285")
result = mycursor.fetchall
 
Watt = []
Hours = []
 
for i in mycursor:
    Watt.append(i[0])
    Hours.append(i[1])

plt.ylabel("Energy Consumption (Joule)",fontname='Times New Roman',fontweight='bold')
plt.xlabel("Time (S)",fontname='Times New Roman',fontweight='bold')
plt.title("Raspberry Pi Power Consumption",fontname='Times New Roman',fontweight='bold')
#plt.plot(Hours, Watt, label = "before attack")
plt.plot(Hours, Watt, 'tab:blue')
#plt.legend();
plt.grid()
plt.show()
