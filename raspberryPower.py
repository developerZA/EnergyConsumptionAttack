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
mycursor.execute("select wat, idd from power11 where watt between 0.282 and 0.285 and idd<=1750")
result = mycursor.fetchall
 
Watt = []
Hours = []
 
for i in mycursor:
    Watt.append(i[0])
    Hours.append(i[1])

     
print("Watt = ", Watt)
print("hours = ", Hours)

mycursor.execute("select wat, idd from power1 where watt > 0.285 and idd<=1750")
result = mycursor.fetchall
 
Watt1 = []
Hours1 = []
 
for i in mycursor:
    Watt1.append(i[0])
    Hours1.append(i[1])



mycursor.execute("select wat, idd from powericmp where watt > 0.285 and idd <=1750")
result = mycursor.fetchall
 
Watticmp = []
Hoursicmp = []
 
for i in mycursor:
    Watticmp.append(i[0])
    Hoursicmp.append(i[1])


mycursor.execute("select wat, idd from powerudp where watt > 0.285 and idd <=1750")
result = mycursor.fetchall
 
Wattudp = []
Hoursudp = []
 
for i in mycursor:
    Wattudp.append(i[0])
    Hoursudp.append(i[1])

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
#ax[0].plot(Hours, Watt, color='black')
#ax[0].set_title("Before Attack", fontweight='bold', fontname='Times New Roman')
#ax[0].grid()
  
# after
ax[0].plot(Hours1, Watt1, color='red', label='After Attack')
ax[0].plot(Hours, Watt, color='blue', label='Before Attack')
ax[0].set_title("After TCP-SYN Attack", fontweight='bold', fontname='Times New Roman')
ax[0].grid()

ax[1].plot(Hoursicmp, Watticmp, color='red')
ax[1].plot(Hours, Watt, color='blue')
#ax[2].plot(Hoursicmp, Watt1)
ax[1].set_title("After ICMP Attack", fontweight='bold', fontname='Times New Roman')
ax[1].grid()

ax[2].plot(Hoursudp, Wattudp, color='red')
ax[2].plot(Hours, Watt, color='blue')
#ax[2].plot(Hoursicmp, Watt1)
ax[2].set_title("After UDP-flood Attack", fontweight='bold', fontname='Times New Roman')
ax[2].grid()
#ax[0].axvline(x=850.22058956,ymin=0.09, ymax=0.70,color='black',ls='--', lw=2, label='Energy Consumption due to attack')

#ax[1].axvline(x=850.22058956,ymin=0.09, ymax=0.83,color='black',ls='--', lw=2)
#ax[2].axvline(x=850.22058956,ymin=0.09, ymax=0.70,color='black',ls='--', lw=2)


fig.text(0.5, 0.04, 'Time (s)', ha='center', fontname='Times New Roman', fontweight='bold', fontsize= 14)
fig.text(0.04, 0.5, 'Energy Consumption (Joule)', fontsize= 14, fontweight='bold', va='center', rotation='vertical', fontname='Times New Roman')
fig.suptitle("Raspberry Pi Energy Consumption", fontname='Times New Roman', fontweight='bold')
plt.rcParams["font.family"] = "Times New Roman"
#ax[0].legend();
ax[0].arrow( 850.0, 1.45, 0.0, 1.03, fc="k", ec="k",head_width=35, head_length=0.1,facecolor='red',length_includes_head=True)
ax[0].arrow( 850.0, 1.45, 0.0, -0.008, fc="k", ec="k",head_width=35, head_length=0.1,color='red',length_includes_head=True )
#ax[0].annotate('Energy Consumption due to attack', xy = (965.4, 1.58), rotation=90.0, fontsize=12,color='black',label="After Attack")
ax[1].arrow( 850.0, 1.45, 0.0, 1.68, fc="k", ec="k",head_width=35, head_length=0.1,facecolor='red',length_includes_head=True)
ax[1].arrow( 850.0, 1.45, 0.0, -0.008, fc="k", ec="k",head_width=35, head_length=0.1,color='red',length_includes_head=True )

ax[2].arrow( 850.0, 1.45, 0.0, 1.01, fc="k", ec="k",head_width=35, head_length=0.1,facecolor='red',length_includes_head=True, label="Energy Consumption due to attack")
ax[2].arrow( 850.0, 1.45, 0.0, -0.008, fc="k", ec="k",head_width=35, head_length=0.1,color='red',length_includes_head=True )
fig.legend(loc='upper right',bbox_to_anchor=(0.90, 0.58), prop={'size': 8})

plt.show()


