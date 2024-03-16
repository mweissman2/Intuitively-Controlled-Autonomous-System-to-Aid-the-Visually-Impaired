"""User_Tracking_Controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
camera_timestep = 33

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
rgb_camera = []
depth_camera = []
gimbal_joints = []

rgb_camera = (robot.getDevice('RGB_camera'))
depth_camera = (robot.getDevice('range_finder'))
rgb_camera.enable(camera_timestep)
depth_camera.enable(camera_timestep)


joint_names = ['gimbal_j1_motor', 'gimbal_j2_motor']
for names in joint_names:
    gimbal_joints.append(robot.getDevice(names))
    
    
#set robot joints
gimbal_joints[0].setPosition(1.3)
gimbal_joints[1].setPosition(0.4)  

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
