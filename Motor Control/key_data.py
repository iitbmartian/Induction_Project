#!/usr/bin/python

import rospy
from std_msgs.msg import String
import sys
import pygame


pygame.init()
display = pygame.display.set_mode((300,300))
    
def publisher():

    rospy.init_node('keyboard_data',anonymous=True)
    pub = rospy.Publisher('keyboard_data_pub',String,queue_size=1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:

                    pub.publish(("FORWARD",1))
                    print("FORWARD")
                if event.key == pygame.K_s:
                    pub.publish(("BACKWARD",1))
                    print("BACKWARD")
                if event.key == pygame.K_a:
                    pub.publish(("LEFT",1))
                    print("LEFT")
                if event.key == pygame.K_d:
                    pub.publish(("RIGHT",1))
                    print("RIGHT")

if __name__ == "__main__":
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass
    

