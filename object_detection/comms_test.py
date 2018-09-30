from time import sleep
import serial
ser = serial.Serial('/dev/cu.usbmodem1441', 9600) # Establish the connection on a specific port
sleep(2) 

 
while 1:      #Do this in loop

    var = raw_input() #get input from user
   
    
    if (var == '1'):
        ser.write('1')
        print ("Right motor one right")
    
    if (var == '2'):
        ser.write('2')
        print ("Right motor one left")

    if (var == '3'):
        ser.write('3') #send 0
        print ("Motor one OFF")

     if (var == '4'):
        ser.write('4')
        print ("Right motor two right")
    
    if (var == '5'):
        ser.write('2')
        print ("Right motor two left")

    if (var == '6'):
        ser.write('6') #send 0
        print ("Motor two OFF")