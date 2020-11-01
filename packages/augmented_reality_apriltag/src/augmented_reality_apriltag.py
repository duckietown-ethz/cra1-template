#!/usr/bin/env python3
import numpy as np
import os
import math
import cv2
from renderClass import Renderer

import rospy
import yaml
import sys
from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError

import rospkg 


"""

This is a template made for the exercise CRA1.
Here you need to project the model in 'models' on an AprilTag, we provide you a 
class that render the obj file.

"""

class Node(DTROS):

    def __init__(self, node_name):

        # Initialize the DTROS parent class
        super(Node, self).__init__(node_name=node_name,node_type=NodeType.GENERIC)        
        self.veh = rospy.get_namespace().strip("/")

        #
        #   Write your code here
        #



    
    def projection_matrix(self, intrinsic, homography):
        """
            Write here you projection matrix, namely the matrix
            that goes from the camera to the AprilTag
        """

    #
    # TEMPLATE CODE
    #

    def readImage(self, msg_image):
        """
            Convert images to OpenCV images
            Args:
                msg_image (:obj:`CompressedImage`) the image from the camera node
            Returns:
                OpenCV image
        """
        try:
            cv_image = self.bridge.compressed_imgmsg_to_cv2(msg_image)
            return cv_image
        except CvBridgeError as e:
            print(e)
            return []

    def readYamlFile(self,fname):
        """
            Reads the file you pass using 'fname'

            E.G. : 
                the calibration file is located in :
                `/data/config/calibrations/filename/DUCKIEBOT_NAME.yaml`
        """
        with open(fname, 'r') as in_file:
            try:
                yaml_dict = yaml.load(in_file)
                return yaml_dict
            except yaml.YAMLError as exc:
                self.log("YAML syntax error. File: %s fname. Exc: %s"
                         %(fname, exc), type='fatal')
                rospy.signal_shutdown()
                return


    def onShutdown(self):
        super(Node, self).onShutdown()


if __name__ == '__main__':
    # Initialize the node
    camera_node = Node(node_name='augmented_reality_apriltag_node')
    # Keep it spinning to keep the node alive
    rospy.spin()