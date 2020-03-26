import cv2 as cv

from Raspberry import ARuco
from Raspberry import Omni
from Raspberry import Serial

ROBOT_ID = 0
DEBUG = True

if __name__ == "__main__":
    ##### Image processing initializations #####
    # Init ARuco module class
    AR = ARuco()

    # Init camera
    cap = cv.VideoCapture(0)

    ##### Calibration #####
    # Final values
    frame_width, ARuco_height = 0, 0

    # Calibration loop
    while not ARuco_height:
        # Get first video frame
        _, frame = cap.read()

        # Detect ARuco marker
        detected_markers = AR.detect_aruco(frame)

        # If detected markers
        if detected_markers:
            # Set frame width
            frame_width = frame.shape[1]

            # Get marker position
            pos = AR.get_marker_pos()

            # Set marker height
            ARuco_height = pos[ROBOT_ID][3]

    ##### Motors processing initializations #####
    # Init Omni platform class
    omni = Omni(frame_width, ARuco_height)

    # Init Serial module class
    serial = Serial()

    ##### Main cycle loop #####
    while True:
        ################################################################
        ##########################Image processing######################
        ################################################################
        # Get current video frame
        ret, frame = cap.read()

        # Detect markers
        detected_markers = AR.detect_aruco(frame)

        # Check if markers are detected
        if detected_markers:
            # Get robot position
            pos = AR.get_marker_pos()

            if DEBUG:
                # Display markers on video frame
                frame = AR.show_aruco()

        if DEBUG:
            # Show result frame
            cv.imshow('image', frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv.destroyAllWindows()
