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
fig, ax = plt.subplots(2)
#fig, (ax1, ax2) = plt.subplots(1, 2)
# Fecthing Data From mysql to my python progame
#FORMAT(watt,3)
mycursor.execute("select wat , idd from f_powerar where watt between 0.212 and 0.213 and idd <=1750")
result = mycursor.fetchall
 
WattAR = []
HoursAR = []
 
for i in mycursor:
    WattAR.append(i[0])
    HoursAR.append(i[1])

     
print("Watt = ", WattAR)
print("hours = ", HoursAR)



mycursor.execute("select wat, idd from f_power where watt between 0.282 and 0.285 and idd <= 1750")
result = mycursor.fetchall
 
WattRP = []
HoursRP = []
 
for i in mycursor:
    WattRP.append(i[0])
    HoursRP.append(i[1])

     
print("Watt = ", WattRP)
print("hours = ", HoursRP)

mycursor.execute("select wat, idd from f_power_ar where idd <=1750")
result = mycursor.fetchall
 
Watt1 = []
Hours1 = []
 
for i in mycursor:
    Watt1.append(i[0])
    Hours1.append(i[1])


mycursor.execute("select wat, idd from f_power_rp where idd <=1750")
result = mycursor.fetchall
 
Watt1s = []
Hours1s = []
 
for i in mycursor:
    Watt1s.append(i[0])
    Hours1s.append(i[1])

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
#ax[0].plot(HoursRP, WattRP,color='black')
#ax[0].set_title("Raspberry Pi Before attack",fontweight='bold',fontname='Times New Roman')
#ax[0].grid()

ax[0].plot(Hours1s, Watt1s, color='red',label='After Attack')
ax[0].plot(HoursRP, WattRP,color='blue',label='Before Attack')
ax[0].set_title("Raspberry Pi After connected to F-AP attack",fontweight='bold',fontname='Times New Roman')
ax[0].grid()
  
# after
#ax[2].plot(HoursAR, WattAR, color='black')
#ax[2].set_title("Arduino Before attack",fontweight='bold',fontname='Times New Roman')
#ax[2].grid()

ax[1].plot(Hours1, Watt1, color='red')
ax[1].plot(HoursAR, WattAR, color='blue')
ax[1].set_title("Arduino After connected to F-AP attack",fontweight='bold',fontname='Times New Roman')
ax[1].grid()

fig.text(0.5, 0.04, 'Time (s)', ha='center',fontsize= 14, fontname='Times New Roman',fontweight='bold')
fig.text(0.04, 0.5, 'Energy Consumption (Joule)', fontsize= 14, fontweight='bold',fontname='Times New Roman', va='center', rotation='vertical')
#fig.suptitle("Arduino and Raspberry Pi Energy Consumption",fontname='Times New Roman',fontweight='bold')


            
#ax[0].axvline(x=850.22058956,ymin=0.07, ymax=0.78,color='black',ls='--', lw=2, label='Energy Consumption due to attack')

#ax[1].axvline(x=850.22058956,ymin=0.07, ymax=0.84,color='black',ls='--', lw=2)


ax[0].arrow( 850.0, 1.49, 0.0, 2.02, fc="k", ec="k",head_width=35, head_length=0.1,facecolor='red',length_includes_head=True,label="Energy Consumption due to attack")
ax[0].arrow( 850.0, 1.49, 0.0, -0.008, fc="k", ec="k",head_width=35, head_length=0.1,color='red',length_includes_head=True )


ax[1].arrow( 850.0, 1.08, 0.0,0.80, fc="k", ec="k",head_width=35, head_length=0.1,facecolor='red',length_includes_head=True)
ax[1].arrow( 850.0, 1.08, 0.0, -0.008, fc="k", ec="k",head_width=35, head_length=0.1,color='red',length_includes_head=True )

fig.legend(loc='upper right',bbox_to_anchor=(0.90, 0.80), prop={'size': 8})
plt.show()




