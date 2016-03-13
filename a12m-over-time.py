import numpy as np
import matplotlib.pyplot as plt
#-------------------------------------------------------------------------------
with open("12mWith.txt", "r") as f:

	rssi_man = []
	for line in f:
		row = line.split(',')
		print len(row[0]);
		#if "3Com" in row[0]:
		if row[0]==" HTC Portable Hotspot ED58":
			#print "hhhhhhhhh"
			#time_man.append(int(row[0]))        		
	        	rssi_man.append(int(row[1]))
		else:
			continue


#-------------------------------------------------------------------------------
with open("12mWithout.txt", "r") as f:
	#time_noman = []
	rssi_noman = []
	for line in f:
		row = line.split(',')
		print len(row[0]);
		#if "3Com" in row[0]: last):
		if row[0]==" HTC Portable Hotspot ED58":
			#print "kkkkk"
			#time_man.append(int(row[0]))        		
	        	rssi_noman.append(int(row[1]))
		else:
			continue
#rssi_man = [3,4,5,6,8]
count= range(0, len(rssi_man))
count2= range(0, len(rssi_noman))
print count
print len(rssi_man)
	#x = np.array([])
'''
binsss= len(rssi_man) +1
n, bins, patches = plt.hist(rssi_man, binsss, normed=1, facecolor='green', alpha=0.75)
l = plt.plot(bins, rssi_man, 'r--', linewidth=1)'''

plt.hist(rssi_man, bins=20)
plt.title("RSSI Histogram 12m")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

plt.title('RSSI variation over the time (12m) ')
plt.xlabel('Count')
plt.ylabel('RSSI (dBm)')
plt.ylim(-100, 0)
plt.plot(count, rssi_man)
plt.plot(count2, rssi_noman)
plt.legend(['Man in LOS', 'Clear LOS'], loc='upper left')
plt.show()
#plt.savefig("text.png", dpi=300)


