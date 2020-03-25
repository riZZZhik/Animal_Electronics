from math import cos, atan2

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

        s1 = self.Kd * cos(alpha + 45)
        s2 = self.Kd * cos(alpha + 135)
        s3 = self.Kd * cos(alpha + 225)
        s4 = self.Kd * cos(alpha + 315)

        return s1, s2, s3, s4

