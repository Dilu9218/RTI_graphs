import numpy as np
import matplotlib.pyplot as plt 

#-------------------------------------------------------------------------------
with open("15mWithTr.txt", "r") as f:

	rssi_man = []
	for line in f:
		row = line.split(',')
		#print len(row[0]);
		#if "3Com" in row[0]:
		if row[0]=="HTC Portable Hotspot ED58":
			print "hhhhhhhhh"
			#time_man.append(int(row[0]))        		
	        	rssi_man.append(int(row[1]))
		else:
			continue


#-------------------------------------------------------------------------------
with open("15mWithRc.txt", "r") as f:
	#time_noman = []
	rssi_noman = []
	for line in f:
		row = line.split(',')
		#print len(row[0]);
		#if "3Com" in row[0]:
		if row[0]=="HTC Portable Hotspot ED58":
			print "kkkkk"
			#time_man.append(int(row[0]))        		
	        	rssi_noman.append(int(row[1]))
		else:
			continue
#rssi_man = [3,4,5,6,8]
count= range(0, len(rssi_man))
count2= range(0, len(rssi_noman))
#print count
#print rssi_man
	#x = np.array([])

plt.title('RSSI variation over the time (15m) ')
plt.xlabel('Count')
plt.ylabel('RSSI (dBm)')
plt.ylim(-100, 0)
plt.plot(count, rssi_man)
plt.plot(count2, rssi_noman)
plt.legend(['Near Tranceiver', 'Near Receiver'], loc='upper left')
plt.show()
#plt.savefig("text.png", dpi=300)


