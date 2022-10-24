# Connecting to mysql database
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
 
 
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="meter")
mycursor = mydb.cursor()
# Initialise the subplot function using number of rows and columns
fig, ax = plt.subplots(3)
#fig, (ax1, ax2) = plt.subplots(1, 2)
# Fecthing Data From mysql to my python progame
mycursor.execute("select wat, idd from powerar1 where watt between 0.212 and 0.213 and idd <= 1750")
result = mycursor.fetchall
 
Watt = []
Hours = []
 
for i in mycursor:
    Watt.append(i[0])
    Hours.append(i[1])

     
print("Watt = ", Watt)
print("hours = ", Hours)

mycursor.execute("select wat, idd from powerar2 where idd <= 1750")
result = mycursor.fetchall
 
Watt1 = []
Hours1 = []
 
for i in mycursor:
    Watt1.append(i[0])
    Hours1.append(i[1])


mycursor.execute("select wat, idd from powerar3 where idd <= 1750")
result = mycursor.fetchall
 
Watt11 = []
Hours11 = []
 
for i in mycursor:
    Watt11.append(i[0])
    Hours11.append(i[1])


mycursor.execute("select wat, idd from powerar4 where idd <= 1750")
result = mycursor.fetchall
 
Watt111 = []
Hours111 = []
 
for i in mycursor:
    Watt111.append(i[0])
    Hours111.append(i[1])
# Visulizing Data using Matplotlib
# plt.bar(Names, Marks)
# plt.ylim(0, 5)
#plt.ylabel("Energy Consumption (A)")
#plt.xlabel("Time (S)")
#plt.title("Raspberry Pi Power Consumption")
#plt.plot(Hours, Watt, label = "before attack")
#plt.plot(Hours1, Watt1, label = "after attack")
#plt.legend();
#plt.show()






# before
#ax[0].plot(Hours, Watt,color='black')
#ax[0].set_title("Before Attack", fontweight='bold', fontname='Times New Roman')
#ax[0].grid()
  
# after
ax[0].plot(Hours1, Watt1, color='red', label='After Attack')
ax[0].plot(Hours, Watt,color='blue', label='Before Attack')
ax[0].set_title("After TCP-SYN Attack", fontweight='bold', fontname='Times New Roman')
ax[0].grid()

ax[1].plot(Hours11, Watt11, color='red')
ax[1].plot(Hours, Watt,color='blue')
ax[1].set_title("After ICMP attack",  fontweight='bold', fontname='Times New Roman')
ax[1].grid()

ax[2].plot(Hours111, Watt111,color='red')
ax[2].plot(Hours, Watt,color='blue')
ax[2].set_title("After UDP Flood attack",  fontweight='bold', fontname='Times New Roman')
ax[2].grid()

#ax[0].axvline(x=850.22058956,ymin=0.09, ymax=0.95,color='black',ls='--', lw=2, label='Energy Consumption due to attack')

#ax[1].axvline(x=850.22058956,ymin=0.09, ymax=0.95,color='black',ls='--', lw=2)
#ax[2].axvline(x=1740,ymin=0.09, ymax=0.95,color='black',ls='--', lw=2)
ax[0].arrow( 850.0, 1.07, 0.0, 0.63, fc="k", ec="k",head_width=35, head_length=0.1,facecolor='red',length_includes_head=True)
ax[0].arrow( 850.0, 1.07, 0.0, -0.008, fc="k", ec="k",head_width=35, head_length=0.1,color='red',length_includes_head=True )
#ax[0].annotate('Energy Consumption due to attack', xy = (965.4, 1.58), rotation=90.0, fontsize=12,color='black',label="After Attack")
#ax[1].arrow( 850.0, 1.07, 0.0, 0.18, fc="k", ec="k",head_width=34, head_length=0.1,facecolor='red',length_includes_head=True)
#ax[1].arrow( 850.0, 1.07, 0.0, -0.009, fc="k", ec="k",head_width=34, head_length=0.1,color='red',length_includes_head=True )

ax[2].arrow( 1750.0, 1.07, 0.0, 0.43, fc="k", ec="k",head_width=35, head_length=0.1,facecolor='red',length_includes_head=True, label="Energy Consumption due to attack")
ax[2].arrow( 1750.0, 1.07, 0.0, -0.008, fc="k", ec="k",head_width=35, head_length=0.1,color='red',length_includes_head=True )

fig.text(0.5, 0.04, 'Time (s)', fontsize= 14, ha='center', fontname='Times New Roman', fontweight='bold')
fig.text(0.04, 0.5, 'Energy Consumption (Joule)',fontsize= 14, fontweight='bold',  fontname='Times New Roman',  va='center', rotation='vertical')
fig.suptitle("Arduino Energy Consumption", fontweight='bold', fontname='Times New Roman')
fig.legend(loc='upper right',bbox_to_anchor=(0.90, 0.85), prop={'size': 8})
plt.rcParams["font.family"] = "Times New Roman"
plt.show()


