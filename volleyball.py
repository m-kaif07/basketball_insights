# count the number of dribbles performed by a player and the number of dribbles per second

import cv2
import numpy as np

def analyze_basketball_dribble(video_path):
    # Loading the video
    cap = cv2.VideoCapture(video_path)

    # dribble_count to store the numbero f dribbles-
    dribble_count = 0
    prev_ball_y = None

    # Parameters for dribble frequency i.e. number of dribbles / sec.
    frame_count = 0
    dribble_time = 0
    fps = cap.get(cv2.CAP_PROP_FPS)

    # using motion detection function to detect only the moving ball / circular object
    fgbg = cv2.createBackgroundSubtractorMOG2()


    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        # background subtraction for motion detection
        fgmask = fgbg.apply(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect ball using HoughCircles
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=10, maxRadius=50)

        if circles is not None:
            # we will filter  out only moving circles, it may consider some other circular things as well. 
            moving_circles = []
            for circle in circles[0]:
                x, y, r = circle.astype(int)
                if fgmask[y, x] == 255:
                    moving_circles.append(circle)
                    if prev_ball_y is not None and y > prev_ball_y:
                        dribble_count += 1
                    prev_ball_y = y

            # draw circle around the moving ball
            for circle in moving_circles:
                x, y, r = circle.astype(int)
                cv2.circle(frame, (x, y), r, (0, 255, 0), 4)

        # Display the number of dribbles on screen
        text = f"No. of Dribbles: {dribble_count}"
        cv2.putText(frame, text, (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), int(1.9))

        # Updating the frame count and dribble time
        frame_count += 1
        if dribble_count > 0:
            dribble_time = round((frame_count / fps), 2)

        # Display the dribble frequency (dribbles / sec)
        text2 = f"Dribbles per second: {dribble_time}"
        cv2.putText(frame, text2, (20, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), int(1.9))
        
        # Display the output video with detected ball
        cv2.imshow('Output', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

    return dribble_count, dribble_count / round(dribble_time)

# input video
video = 'basketball_insights/basketball.mp4'

# Analyze the basketball dribble video
dribble_count, dribble_frequency = analyze_basketball_dribble(video)

# Print the results
print("Number of dribbles performed : ", dribble_count)
print("Dribble frequency : ", dribble_frequency)