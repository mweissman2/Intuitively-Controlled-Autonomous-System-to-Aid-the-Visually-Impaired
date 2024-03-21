from controller import robot
import cv2 as cv
import numpy as np
from controller import CameraRecognitionObject
#class for gimbal that can be instantiated multiple times
class Gimbal_Controller:
    def __init__(self, rgb_camera, depth_camera, gimbal_joints, update_time):
        #set references to simulation objects
        self.rgb_camera = rgb_camera
        self.depth_camera = depth_camera
        self.z_axis_motor = gimbal_joints[0]
        self.y_axis_motor = gimbal_joints[1]

        #define other initialization stuff
        self.starting_z_axis_angle = 0
        self.starting_y_axis_angle = 0

        self.current_z_axis_angle = 0
        self.current_y_axis_angle = 0
        self.update_time = update_time
        self.user_id = 30


    def set_user_id(self, user_id):
        self.user_id = user_id
    def enable_segmentation(self, status):
        if status == False:
            #disable segmentation
            self.rgb_camera.disableRecognitionSegmentation()
        else:
            #enable segmentation
            self.rgb_camera.enableRecognitionSegmentation()

    def enable_recognition(self, status):
        if status == False:
            #disable recognition
            self.rgb_camera.recognitionDisable()
        else:
            #enable recognition
            self.rgb_camera.recognitionEnable(self.update_time)

    def center_user(self):
        return 0
    def find_user(self):
        objects = self.rgb_camera.getRecognitionObjects()
        for obj in objects:
            if obj.getId() == self.user_id:
                position = obj.getPosition()
                position_on_image = obj.getPositionOnImage()
                print(position_on_image[0])

    def enable_vision(self, status):
        self.enable_recognition(status)
        self.enable_segmentation(status)

    def process_image(self, image):
        return 0

    def segment_image(self, image):
        return 0

    def calculate_depth(self,depth_image):
        return 0

    def get_depth_image(self):
        image_c_ptr = self.depth_camera.getRangeImage(data_type="buffer")
        image_np = np.ctypeslib.as_array(image_c_ptr, (self.depth_camera.getWidth() * self.depth_camera.getHeight(),))
        return image_np

    def calculate_angle(self):
        return 0

    def calculate_user_position(self):
        return 0

    def interpolate_velocity(self):
        return 0

    def estimate_next_position(self):
        return 0



