from pirc522 import RFID

import signal
import time

rdr = RFID()
util = rdr.util()
util.debug = True

def read_id():
	while True:
		#Request tag
		(error, data) = rdr.request()
		if not error:
			print ("\nDetected")
			(error, uid) = rdr.anticoll()
			if not error:
		        #Print UID
				value = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
				print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
				if (value === "25,114,39,43"):
					print "Name:Rahul \n Age: 20\nBlood Group: AB+ve\nPhone No. : 8904876227"
				if (value === "61,243,140,101"):
					print "Name:Amitosh \n Age: 35\nBlood Group: A+ve\nPhone No. : 9090487389"
				if (value === "166,56,193,50"):
					print "Name:Sumeet \n Age: 30\nBlood Group: O+ve\nPhone No. : 8904876436"
				if (value === "133,241,222,82"):
					print "Name:Shiba \n Age: 25\nBlood Group: B+ve\nPhone No. : 7478748227"
				time.sleep(1)
				
