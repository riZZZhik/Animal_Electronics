from adafruit_servokit import ServoKit


class Servo:
    """Class for handling servo motors"""
    def __init__(self, channels=16):
        """Initialize main variables of this class
        :param channels: number of servo channels in ServoKit (8 or 16)
        """
        self.kit = ServoKit(channels=channels)

    def set_motor(self, motor_id, angle):
        """Function to set servo motor angle
        :param motor_id: motor id
        :param angle: angle to be set
        """
        self.kit.servo[motor_id].angle = angle

    def set_all_motors(self, angle_list):
        """Function to set angle for each servo motor
        :param angle_list: angles to be set on each motors
        """
        for i, angle in enumerate(angle_list):
            self.kit.servo[i].angle = angle
