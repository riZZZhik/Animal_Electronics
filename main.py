import cv2 as cv
from Raspberry import ARuco

DEBUG = True

if __name__ == "__main__":
    # Init ARuco module class
    AR = ARuco()

    # Init camera
    cap = cv.VideoCapture(0)

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
            pos = AR.get_robot_pos()

            if DEBUG:
                # Display robot position
                cv.putText(frame, str(pos), (20, 30 * len(pos)), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

                # Display markers on video frame
                frame = AR.show_aruco()

        if DEBUG:
            # Show result frame
            cv.imshow('image', frame)

    cap.release()
    cv.destroyAllWindows()
