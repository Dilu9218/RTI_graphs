import numpy as np
import matplotlib.pyplot as plt


average_rssi_noman = []
average_rssi_man = []
#time_noman = []
#time_man = []

#-------------------------------------------------------------------------------
with open("2mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		if line.startswith(' ') or line.startswith('-'): 
			continue
		row = line.split(',')      
		#print int(row[1])	
		if row[0]=="HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
		#print count
	average_rssi_man.append(int(sum_rssi/count))
	#time_noman.append(2) 

with open("2mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		if line.startswith(' ') or line.startswith('-'): 
			continue
		row = line.split(',')      		
		if row[0]=="HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	#print count
	average_rssi_noman.append(int(sum_rssi/count))
	#time_man.append(2)

#-------------------------------------------------------------------------------
with open("4mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		if line.startswith(' ') or line.startswith('-'): 
			continue
		row = line.split(',')      		
		if row[0]=="HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_man.append(int(sum_rssi/count))
	#time_noman.append(2) 

with open("Recheck4mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		if line.startswith(' ') or line.startswith('-'): 
			continue
		row = line.split(',')      		
		if row[0]=="HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))
	#time_man.append(2)

#-------------------------------------------------------------------------------
with open("6mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      	
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_man.append(int(sum_rssi/count))

with open("6mWithout2.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      		
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))

#-------------------------------------------------------------------------------
with open("8mWith2.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      
			
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
		
	average_rssi_man.append(int(sum_rssi/count))
	

with open("8mWithout2.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      		
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	
	average_rssi_noman.append(int(sum_rssi/count))
	

#-------------------------------------------------------------------------------
with open("10mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		if line.startswith(' ') or line.startswith('-'): 
			continue
		row = line.split(',')      		
		if row[0]=="HTC Portable Hotspot ED58":	
			 sum_rssi = sum_rssi + int(row[1])
			 count = count + 1
	average_rssi_man.append(int(sum_rssi/count))
	#time_noman.append(2) 

with open("10mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		if line.startswith(' ') or line.startswith('-'): 
			continue
		row = line.split(',')      		
		if row[0]=="HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))
	#time_man.append(2)

#-------------------------------------------------------------------------------
with open("12mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		'''if line.startswith(' ') or line.startswith('-'): 
			continue'''
		row = line.split(',')      
		#print int(row[1])	
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
		#print count
	average_rssi_man.append(int(sum_rssi/count))
	#time_noman.append(2) 

with open("12mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		'''if line.startswith(' ') or line.startswith('-'): 
			continue'''
		row = line.split(',')      		
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	#print count
	average_rssi_noman.append(int(sum_rssi/count))
	#time_man.append(2)

#-------------------------------------------------------------------------------
with open("14mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      	
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_man.append(int(sum_rssi/count))

with open("14mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      		
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))


#-------------------------------------------------------------------------------
with open("16mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      	
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_man.append(int(sum_rssi/count))

with open("16mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      		
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))

#-------------------------------------------------------------------------------
with open("18mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      	
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_man.append(int(sum_rssi/count))

with open("18mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      		
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))

#-------------------------------------------------------------------------------
with open("20mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      	
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_man.append(int(sum_rssi/count))

with open("20mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      		
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))

#-------------------------------------------------------------------------------
with open("22mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      	
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_man.append(int(sum_rssi/count))

with open("22mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      		
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))

#-------------------------------------------------------------------------------
with open("25mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      	
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_man.append(int(sum_rssi/count))

with open("25mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      		
		if row[0]==" HTC Portable Hotspot ED58":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))
#-------------------------------------------------------------------------------
with open("30mWith.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      	
		if row[0]=="AndroidAP0787":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_man.append(int(sum_rssi/count))

with open("30mWithout.txt", "r") as f:	
	sum_rssi = 0
	count = 0
	for line in f:
		row = line.split(',')      		
		if row[0]=="AndroidAP0787":	
			sum_rssi = sum_rssi + int(row[1])
			count = count + 1
	average_rssi_noman.append(int(sum_rssi/count))



#count1= range(0, len(average_rssi_man))
#print count
count1= [2,4,6,8,10,12,14,16,18,20,22,25,30]
count2= [2,4,6,8,10,12,14,16,18,20,22,25,30]
#count2= range(0, len(average_rssi_noman))
#count2= [2,4,10]
print average_rssi_man
print average_rssi_noman
plt.title('Average RSSI variation with the distance')
plt.xlabel('Distance (m)')
plt.ylabel('Average RSSI (dBm)')
plt.grid(True)
plt.ylim(-100, -10)
plt.plot(count1, average_rssi_man, marker="o", label= 'Man in los')
plt.plot(count2, average_rssi_noman, marker="o", label= 'Clear los')
plt.legend(['Man in LOS', 'Clear LOS'], loc='upper left')
plt.show()
#plt.savefig("text.png", dpi=300)


