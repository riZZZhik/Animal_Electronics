import math

import cv2 as cv
import cv2.aruco as aruco


class ARuco:
    """Class for detecting ARuco markers on frame"""

    def __init__(self, aruco_type=aruco.DICT_4X4_250):
        """Initialize main variables of this class
        :param aruco_type: aruco_type, search for values in cv2.aruco module
        """
        # Init class image variable
        self.img = None

        # Init values for ARuco detection
        self.detected_markers = {}
        self.robot_pos = {}
        self._aruco_dict = aruco.Dictionary_get(aruco_type)
        self._aruco_parameters = aruco.DetectorParameters_create()

    def detect_aruco(self, img):
        """Function to detect markers on image
        :param img: Image to detect markers
        :return: List of ARuco detected markers
        """
        # Save image to class variable
        self.img = img

        # Convert image to gray scale
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Detect ARuco markers
        corners, ids, _ = aruco.detectMarkers(gray, self._aruco_dict, parameters=self._aruco_parameters)

        # Save detected markers to list
        self.detected_markers = {}
        if len(corners):
            for k in range(len(corners)):
                temp_1 = corners[k]
                temp_1 = temp_1[0]
                temp_2 = ids[k]
                temp_2 = temp_2[0]
                self.detected_markers[temp_2] = temp_1
        return self.detected_markers

    def show_aruco(self):
        """Function to display ARuco markers centre, direction and id
        :return: Marked image
        """
        key_list = self.detected_markers.keys()
        font = cv.FONT_HERSHEY_SIMPLEX

        robot_pos_text = "%d: X=%d; Y=%d; A=%d; H=%d"
        self.get_marker_pos()

        for key in key_list:
            dict_entry = self.detected_markers[key]

            centre, top_centre = self._get_marker_centres(dict_entry)

            cv.line(self.img, centre, top_centre, (0, 255, 0), 3)
            cv.circle(self.img, centre, 1, (0, 0, 255), 6)
            cv.putText(self.img, str(key), (int(centre[0] + 20), int(centre[1])), font, 1, (0, 0, 255), 2, cv.LINE_AA)
            cv.putText(self.img, robot_pos_text % ((key,) + self.robot_pos[key].items()),
                       (20, 30 * len(key_list)), font, 1, (0, 0, 255), 2, cv.LINE_AA)

        return self.img

    def get_marker_pos(self):
        """Function to give the position of the robot (centre(x), centre(y), angle, height).
        :return: Dictionary of robots positions
        """
        self.robot_pos = {}
        key_list = self.detected_markers.keys()

        for key in key_list:
            dict_entry = self.detected_markers[key]
            pt1, pt2 = tuple(dict_entry[0]), tuple(dict_entry[1])

            centre, top_centre = self._get_marker_centres(dict_entry)

            angle = self._angle_calculate(pt1, pt2)

            height = self._distance_calculate(centre, top_centre)

            self.robot_pos[key] = {"X": int(centre[0]), "Y": int(centre[1]),
                                   "Angle": angle, "ARuco_height": height}

        return self.robot_pos

    @staticmethod
    def _get_marker_centres(corners):
        """Function to calculate centre and top_centre of marker
        :param corners: list of ARuco marker corners
        :return: centre and top_centre
        """
        centre = corners[0] + corners[1] + corners[2] + corners[3]
        centre[:] = [int(x / 4) for x in centre]
        centre = tuple(centre)
        top_centre = tuple((corners[0] + corners[1]) / 2)
        return centre, top_centre

    @staticmethod
    def _angle_calculate(pt1, pt2):
        """Function to calculate angle between two points in the range of 0-359
        :param pt1: Position of first point (x, y)
        :param pt2: Position of second point (x, y)
        :return: angle between two points
        """
        angle_list = list(range(359, 0, -1))
        angle_list = angle_list[-90:] + angle_list[:-90]
        x = pt2[0] - pt1[0]
        y = pt2[1] - pt1[1]
        angle = int(math.degrees(math.atan2(y, x)))
        angle = angle_list[angle]
        return int(angle)

    @staticmethod
    def _distance_calculate(pt1, pt2):
        """Function to calculate distance between two points
        :param pt1: Position of first point (x, y)
        :param pt2: Position of second point (x, y)
        :return: distance between two points
        """
        dist = math.sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
        return dist
