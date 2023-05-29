#!/usr/bin/python3


import rospy
import cv2
import numpy as np
from geometry_msgs.msg import Point

def webcam_callback(frame):
    # Create a ROS publisher for the centroid point
    centroid_pub = rospy.Publisher("centroid", Point, queue_size=10)
    
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the lower and upper bounds for green color in HSV
    lower_green = np.array([40, 100, 50])
    upper_green = np.array([80, 255, 255])
    
    # Threshold the image to get only the green regions
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    
    # Find contours of the green regions
    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find the largest contour (assuming it corresponds to the green object)
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Calculate the centroid of the largest contour
        moments = cv2.moments(largest_contour)
        
        if moments["m00"] != 0:    
            
            centroid_x = int(moments["m10"] / moments["m00"])
            centroid_y = int(moments["m01"] / moments["m00"])
            
            # Create a Point message with the centroid coordinates
            centroid_msg = Point(x=centroid_x, y=centroid_y, z=0)
            
            # Publish the centroid message
            centroid_pub.publish(centroid_msg)
            
            # Draw a circle at the centroid location
            cv2.circle(frame, (centroid_x, centroid_y), 5, (0, 255, 0), -1)
    
    # Show the frame with detection
    cv2.imshow("Webcam Detection", frame)
    cv2.waitKey(1)

def webcam_node():
    rospy.init_node("webcam_node")
    

    
    # Create a OpenCV capture object to access the webcam
    cap = cv2.VideoCapture(0)
    
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        
        # Process the frame and detect the green object
        webcam_callback(frame)
        
        # Sleep for a small duration
        rospy.sleep(0.1)

    # Release the capture object and shutdown the node
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        # Start the webcam node
        webcam_node()

    except rospy.ROSInterruptException:
        pass
