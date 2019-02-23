
from udacidrone import Drone
from udacidrone.connection import MavlinkConnection

#Now you can initialize the drone with the following commands:
conn = MavlinkConnection('tcp:127.0.0.1:5760', threaded=True)
drone = Drone(conn)
drone.start()

#Now take control of the drone and arm the rotors. Briefly pause in between executing code snippets as running them in immediate succession can cause strange drone behavior within the simulator.
drone.take_control()
drone.arm()


#Now set the drone's "home position"
drone.set_home_position(drone.global_position[0],
                        drone.global_position[1],
                        drone.global_position[2])

#And now you can take off (to a height of 3 meters)!
drone.takeoff(3)

#Once you're in the air, you can fly around by commanding the drone to waypoints.
drone.cmd_position(5,0,3,0)

"""
There are many commands you can issue to the drone through this API. Some of them include...

start()
: Start receiving messages from the drone. If the connection is not threaded, this will block the code

stop()
: Terminate the connection with the drone and close the telemetry log

take_control()
: Set the command mode of the quad to guided.

release_control()
: Set the command mode of the quad to manual.

arm()
: Arms the motors of the quad, the rotors begin spinning. The drone cannot takeoff until armed.

disarm()
: Disarms the motors of the quad. The quadcopter cannot be disarmed in the air.

cmd_position(north, east, down, heading)
: Command the vehicle to travel to the local position (north, east, down). Also commands the quad to maintain a specified heading.
"""
