import cv2 as cv
import time

from Raspberry import *

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
        if detected_markers[ROBOT_ID]:
            # Set frame width
            frame_width = frame.shape[1]

            # Get marker position
            pos = AR.get_marker_pos()

            # Set marker height
            ARuco_height = pos[ROBOT_ID]["ARuco_height"]

    ##### Motors processing initializations #####
    # Init Omni platform class
    omni = Omni(frame_width, ARuco_height)

    # Init scenes class
    scenes = Scenes()

    # Init Serial module class
    serial = Serial()

    # Init Servo motors class
    servo = Servo()

    ##### Waiting for signal to begin #####
    while not serial.read():
        time.sleep(0.5)

    ##### Main cycle loop #####
    scene_running = False
    start_time = time.time()
    while True:
        # Exit after two minutes
        if time.time() - start_time > 120:
            break

        ################################################################
        ##########################Image processing######################
        ################################################################
        # Get current video frame
        ret, frame = cap.read()

        # Detect markers
        detected_markers = AR.detect_aruco(frame)
        pos = {}

        # Check if markers detected
        if detected_markers[ROBOT_ID]:
            # Get robot position
            pos = AR.get_marker_pos()[ROBOT_ID]

        if DEBUG:
            # Display markers on video frame
            frame = AR.show_aruco()

            # Show result frame
            cv.imshow('image', frame)

            # Exit if "q" button pressed
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        ################################################################
        #########################Scenes processing######################
        ################################################################
        scene_id = 0  # TODO: Code for listening audio channel
        scenes.scene(scene_id)

        ################################################################
        #########################Motors processing######################
        ################################################################
        # Send speeds to motors if needed
        if pos and scenes.scene_aruco:
            speeds = omni.ARuco_regulator(pos["X"], pos["ARuco_height"])
            serial.send_speeds(speeds, 0)

    cap.release()
    cv.destroyAllWindows()
