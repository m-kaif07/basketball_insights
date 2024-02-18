Basketball Dribble Counting Program : 
This program analyzes a basketball dribble video to count the number of dribbles performed by the player and calculates the dribble frequency (dribbles per second). It utilizes computer vision techniques, including motion detection and circle detection, to extract meaningful insights from the video footage.

Features:
Dribble Counting: Detects and counts each dribble performed by the player by tracking the movement of the basketball.
Dribble Frequency Analysis: Calculates the frequency of dribbles in dribbles per second, providing insights into the player's dribbling performance over time.
Motion Detection: Uses background subtraction to identify moving objects in the video frames, focusing on the basketball's movement.
Circle Detection (HoughCircles): Applies the Hough Circle Transform to detect circular objects in the video frames, assuming the basketball is a circular object.
How to Use:
Input Video:
Provide the path to the input video file (basketball.mp4) in the program.
Run the Program:
Execute the program, and it will analyze the basketball dribble video automatically.
View Results:
The program will display the number of dribbles performed by the player and the dribble frequency (dribbles per second) on the output video.
Additionally, the results will be printed to the console.
Dependencies:
Python (3.x recommended)
OpenCV (4.x recommended)
Usage Example:
python
Copy code
python basketball_dribble_counter.py
Additional Notes:
Adjust parameters in the program (e.g., Hough Circle parameters) as needed to optimize performance for different video footage.
Ensure proper lighting conditions and camera angle for accurate detection of the basketball and dribble movements.
This program serves as a tool for analyzing basketball dribble videos and extracting insights for performance evaluation and training purposes.
Contributors:
Mohammad Kaif
Feel free to contribute, report issues, or suggest improvements to this program. Happy dribbling! 🏀✨
