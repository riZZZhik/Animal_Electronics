import math

import cv2 as cv
import cv2.aruco as aruco


class ARuco:
    """Class for detecting and working with ARuco markers on image"""
    def __init__(self, aruco_type=aruco.DICT_4X4_250):
        """Initialize main variables of this class
        :param aruco_type: aruco_type, search for values in cv2.aruco module
        """
        # Init class image variable
        self.img = None

        # Init values for ARuco detection
        self.detected_markers = {}
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

        for key in key_list:
            dict_entry = self.detected_markers[key]
            centre = dict_entry[0] + dict_entry[1] + dict_entry[2] + dict_entry[3]
            centre[:] = [int(x / 4) for x in centre]  # finding the centre
            centre = tuple(centre)
            orient_centre = tuple((dict_entry[0] + dict_entry[1]) / 2)

            cv.line(self.img, centre, orient_centre, (0, 255, 0), 3)
            cv.circle(self.img, centre, 1, (0, 0, 255), 6)
            cv.putText(self.img, str(key), (int(centre[0] + 20), int(centre[1])), font, 1, (0, 0, 255), 2, cv.LINE_AA)
        return self.img

    def get_robot_pos(self):
        """Function to give the position of the robot (centre(x), centre(y), angle)
        :return: Dictionary of robots position
        """
        robot_state = {}
        key_list = self.detected_markers.keys()

        for key in key_list:
            dict_entry = self.detected_markers[key]
            pt1, pt2 = tuple(dict_entry[0]), tuple(dict_entry[1])

            centre = dict_entry[0] + dict_entry[1] + dict_entry[2] + dict_entry[3]
            centre[:] = [int(x / 4) for x in centre]
            centre = tuple(centre)

            angle = self._angle_calculate(pt1, pt2)
            
            robot_state[key] = (int(centre[0]), int(centre[1]), angle)

        return robot_state

    @staticmethod
    def _angle_calculate(pt1, pt2):
        """Function to calculate angle between two points in the range of 0-359
        :return: angle between two points
        """
        angle_list = list(range(359, 0, -1))
        angle_list = angle_list[-90:] + angle_list[:-90]
        x = pt2[0] - pt1[0]
        y = pt2[1] - pt1[1]
        angle = int(math.degrees( math.atan2(y, x)))
        angle = angle_list[angle]
        return int(angle)


if __name__ == "__main__":
    # Init ARuco class
    AR = ARuco()

    # Init camera
    cap = cv.VideoCapture(0)

    while True:
        # Get current video frame
        ret, frame = cap.read()

        # Detect markers
        detected_markers = AR.detect_aruco(frame)

        # Check if markers are detected
        if detected_markers:
            # Get robot position
            print(AR.get_robot_pos())

            # Display markers on video frame
            frame = AR.show_aruco()

        # Show result frame
        cv.imshow('image', frame)

        # Exit if "q" is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
