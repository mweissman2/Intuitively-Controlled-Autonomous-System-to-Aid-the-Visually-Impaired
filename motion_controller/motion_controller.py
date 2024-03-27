from controller import robot
import numpy as np

class MotionController:
    def __init__(self, wheel1, wheel2, wheel3, wheel4):
        self.inside_wheel_1 = wheel1
        self.inside_wheel_2 = wheel3
        self.outside_wheel_1 = wheel2
        self.outside_wheel_2 = wheel4

        self.current_position = [0,0]
        self.current_heading = 0


    def set_forward_velocity(self, velocity):
        return 0

    def set_forward_position(self, distance):
        return 0

    def set_left_velocity(self, velocity):
        return 0

    def set_left_position(self, distance):
        return 0

    def set_right_velocity(self, velocity):
        return 0

    def set_right_position(self, distance):
        return 0

    def set_turn_velocity(self, velocity):
        return 0

    def set_turn_position(self, angle):
        return 0

    def set_turn_virtual_center(self, angle):
        return 0

    def set_turn_virtual_center_velocity(self, velocity):
        return 0

    def get_current_position(self):
        return self.current_position

    def set_current_position(self, new_position):
        self.current_position = new_position

    def get_heading(self):
        return self.current_heading

    def set_heading(self, new_heading):
        self.current_heading = new_heading

    def get_encoder_reading(self, wheel):
        return 0

    def at_goal_position(self, goal_position):
        return False