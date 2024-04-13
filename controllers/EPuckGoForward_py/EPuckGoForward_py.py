from controller import Robot, DistanceSensor, Motor
import numpy, cv2
# time in [ms] of a simulation step
def run_robot(robot):
    timestep=64
    MAX_SPEED = 6.28
    # gps=robot.getDevice('gps')
    # gps.enable(timestep)
    leftMotor=robot.getDevice('motor_left')
    rightMotor=robot.getDevice('motor_right')
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(0.0)
    rightMotor.setVelocity(0.0)
    leftSensor=robot.getDevice('sensor_left')
    leftSensor.enable(timestep)
    rightSensor=robot.getDevice('sensor_right')
    rightSensor.enable(timestep)
    leftSpeed  = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED
    while robot.step(timestep)!=-1:
        print("#################")
        print(str(leftSensor.getValue())+"##"+str(rightSensor.getValue()))
        # print('GPS X' + str(gps.getValues()[0]))
        # print('GPS Y' + str(gps.getValues()[1]))
        # print('GPS Z' + str(gps.getValues()[2]))
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(rightSpeed)

if __name__=='__main__':
    my_robot=Robot()
    run_robot(my_robot)