import numpy as np
import matplotlib.pyplot as plt 

#-------------------------------------------------------------------------------
'''with open("c", "r") as f:

	rssi_man = []
	for line in f:
		row = line.split(',')
		print len(row[0]);
		#if "3Com" in row[0]:
		if row[0]=="HTC Portable Hotspot ED58":
			print "hhhhhhhhh"
			#time_man.append(int(row[0]))        		
	        	rssi_man.append(int(row[1]))
		else:
			continue
'''

#-------------------------------------------------------------------------------
"""with open("../results-2015-12-09-processed/2m-noman.txt", "r") as f:
	time_noman = []
	rssi_noman = []
	for line in f:
		if not line.strip() or line.startswith('@') or line.startswith('#'): 
			continue
		else:
			row = line.split(' ')
        		time_noman.append(int(row[0]))        		
		        rssi_noman.append(int(row[1]))

"""
rssi_man = [3,4,5,6,8]
count= range(0, len(rssi_man))
print count
print rssi_man
	#x = np.array([])

plt.title('RSSI variation over the time (2m) ')
plt.xlabel('Count')
plt.ylabel('RSSI (dBm)')
plt.ylim(-100, 0)
plt.plot(count, rssi_man)
#plt.plot(time_noman, rssi_noman)
plt.legend(['Man in LOS', 'Clear LOS'], loc='upper left')
plt.show()
#plt.savefig("text.png", dpi=300)


