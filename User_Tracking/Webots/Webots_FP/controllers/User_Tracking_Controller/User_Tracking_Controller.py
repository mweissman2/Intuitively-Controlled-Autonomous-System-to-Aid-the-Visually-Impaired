"""User_Tracking_Controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Supervisor
import Gimbal_Controller as GC

robot = Supervisor()
#get ID of user for tracking.
user_node = robot.getFromDef('USER')
user_id = user_node.getId()
# create the Robot instance.
#my_robot = robot.getFromDef('DOG')



# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
camera_timestep = 32

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
    


tracker = GC.Gimbal_Controller(rgb_camera, depth_camera, gimbal_joints,camera_timestep)
#enables computer vision and sets the ID for user recognition
tracker.enable_tracking(True)
tracker.set_user_id(user_id)
print("Tracking started")
# Main loop:
# - perform simulation steps until Webots is stopping the controller
i = 0
while robot.step(timestep) != -1:
    # Read the sensors:
    if i == 3:
        tracker.find_user()
        i = 0
    i += 1
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
