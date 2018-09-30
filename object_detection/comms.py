#############

## Modified and used as open source


#!/usr/bin/env python

'''
Track a green ball using OpenCV.

    Copyright (C) 2015 Conan Zhao and Simon D. Levy

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as 
    published by the Free Software Foundation, either version 3 of the 
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License 
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import cv2
import numpy as np
from time import sleep
import serial


# For OpenCV2 image display
WINDOW_NAME = 'GreenBallTracker' 

def track(image, on_target, count=0):

    # Assume no centroid
    ctr = (-1,-1)
    total_y_center = int(round(image.shape[0]/2))
    total_x_center = int(round(image.shape[1]/2))

    if not count % 10 == 0:
        return ((ctr), (total_x_center,total_y_center))

    '''Accepts BGR image as Numpy array
       Returns: (x,y) coordinates of centroid if found
                (-1,-1) if no centroid was found
                None if user hit ESC
    '''

    # Blur the image to reduce noise
    blur = cv2.GaussianBlur(image, (5,5),0)
    #image = image[200:800, 400:1500]

    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image for only green colors
    lower_green = np.array([40,70,70])
    upper_green = np.array([80,200,200])

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Blur the mask
    bmask = cv2.GaussianBlur(mask, (5,5),0)

    # Take the moments to get the centroid
    moments = cv2.moments(bmask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)



    print(image.shape)
    if on_target:
        cv2.circle(image, (total_x_center,total_y_center), 50, (0,255,0))
    else:
        cv2.circle(image, (total_x_center,total_y_center), 50, (0,0,255))

    # Use centroid if it exists
    if centroid_x != None and centroid_y != None:

        ctr = (centroid_x, centroid_y)

        cv2.circle(image, ctr, 50, (0,0,0))
        print(round(total_x_center),int(round(total_y_center))),(int(round(centroid_x)),int(round(centroid_y)))
        cv2.line(image,(int(round(total_x_center)),int(round(total_y_center))),(int(round(centroid_x)),int(round(centroid_y))),(0,0,0),5)

    # Display full-color image
    cv2.imshow(WINDOW_NAME, image)

    # Force image display, setting centroid to None on ESC key input
    if cv2.waitKey(1) & 0xFF == 27:
        ctr = None
    
    # Return coordinates of centroid
   # print(ctr)
    return (ctr, (total_x_center,total_y_center))
###########



def motor_1_right():
    ser.write('1')
    print ("motor one right")

def motor_1_left():
    ser.write('2')
    print ("motor one left")

def motor_1_off():
    ser.write('3') #send 0
    print ("Motor one OFF")

def motor_2_right():
    ser.write('4')
    print ("motor two right")

def motor_2_left():
    ser.write('5')
    print ("motor two left")

def motor_2_off():
    ser.write('6') #send 0
    print ("Motor two OFF")


ser = serial.Serial('/dev/cu.usbmodem1441', 9600) # Establish the connection on a specific port
sleep(2) 

LIMIT = 5
CENTER = 75
 
# Test with input from camera
if __name__ == '__main__':

    motor_one_left = 0
    motor_one_right = 0
    motor_two_left = 0
    motor_two_right = 0

    capture = cv2.VideoCapture(1)
    on_target = False

    while True:

        okay, image = capture.read()

        if okay:
            corr, center = track(image, on_target)

            if cv2.waitKey(1) & 0xFF == 27:
                break

            print(corr[0], corr[1])

            ##Reset
            motor_1_off()
            motor_2_off()
            if (corr[0] == -1 and corr[1] == -1):
                continue

            ## Within 100px stay still
            if abs(corr[0] - center[0]) < CENTER:
                motor_1_off()
            elif (corr[0] - center[0]) > 0 and motor_1_right <= LIMIT:
                motor_1_right()
                motor_one_right+=1
                motor_one_left-=1
            elif motor_one_left <= LIMIT:
                motor_1_left()
                motor_one_left+=1
                motor_one_right-=1


            if abs(corr[1] - center[1]) < CENTER:
                motor_2_off()
            elif (corr[1] - center[1]) > 0 and motor_two_right <= LIMIT:
                motor_2_right()
                motor_two_right+=1
                motor_two_left-=1
            elif motor_two_left <= LIMIT: 
                motor_2_left()
                motor_two_left+=1
                motor_two_right-=1


            if abs(corr[0] - center[0]) < CENTER and abs(corr[1] - center[1]) < CENTER:
                 on_target = True
            else:
                on_target = False



        else:

           print('Capture failed')
           break

