import cv2 as cv

from Raspberry import ARuco

DEBUG = True

if __name__ == "__main__":
    ##### Image processing initializations #####
    # Init ARuco module class
    AR = ARuco()

    # Init camera
    cap = cv.VideoCapture(0)

    # Get first video frame
    _, frame = cap.read()

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
