from math import atan2, cos, radians as rad

class Omni:
    """Class for getting speeds for omni wheel platform"""

    def __init__(self, x_width, aruco_height, Kx=1, Ky=1, Kd=1):
        """Initialize main variables.
        :param x_width: Width of frame
        :param aruco_height: Height of ARuco marker in start position

        :param Kx: coefficient for X aruco regulator
        :param Ky: coefficient for Y aruco regulator
        :param Kd: coefficient for decart regulator
        """
        self.x_center = x_width / 2
        self.y_start = aruco_height
        
        self.Kx = Kx
        self.Ky = Ky
        self.Kd = Kd

    def decart_regulator(self, x, y):
        """Function for get speeds on wheels with decart system positions.
        :param x: Needed X position in decart system
        :param y: Needed Y position in decart system"""
        alpha = atan2(y, x)

        s1 = self.Kd * cos(alpha + rad(45)) * 255
        s2 = self.Kd * cos(alpha + rad(135)) * 255
        s3 = self.Kd * cos(alpha + rad(225)) * 255
        s4 = self.Kd * cos(alpha + rad(315)) * 255

        return s1, s2, s3, s4

    def ARuco_regulator(self, x_pos, y_height):
        """Function for get speeds on wheels with information from ARuco marker.
        :param x_pos: Current position of ARuco marker
        :param y_height: Current height of ARuco marker"""
        y_range = self.y_start - y_height
        f = y_range * self.Ky if y_range > 50 else 0

        x_range = (x_pos - self.x_center)
        h = x_range * self.Kx if x_range > 100 else 0

        s1 =
        s2 =
        s3 =
        s4 =

        return s1, s2, s3, s4

    def ARuco_calibrate(self, aruco_height):
        """Function for calibrate ARuco default height.
        :param aruco_height: Height of ARuco marker in start position
        """
        self.y_start = aruco_height
