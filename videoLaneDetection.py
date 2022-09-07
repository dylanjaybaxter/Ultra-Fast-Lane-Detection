import cv2
import time
#import pafy
from ultrafastLaneDetector import UltrafastLaneDetector, ModelType

model_path = "models/tusimple_18.pth"
model_type = ModelType.TUSIMPLE
use_gpu = True

# Initialize video
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Capture Failed")
    cap = None
w = int(cap.get(3))
h = int(cap.get(4))
size = (w,h)
print(size)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter('./test.mp4',fourcc,20.0,size)

#videoUrl = 'https://youtu.be/2CIxM7x-Clc'
#videoPafy = pafy.new(videoUrl)
#print(videoPafy.streams)
#cap = cv2.VideoCapture(videoPafy.streams[-1].url)

# Initialize lane detection model
lane_detector = UltrafastLaneDetector(model_path, model_type, use_gpu)

cv2.namedWindow("Detected lanes", cv2.WINDOW_NORMAL)	

while cap.isOpened():

    # Read frame from the video
    ret, frame = cap.read()

    if ret:	
        t1 = time.clock()

        # Detect the lanes
        output_img = lane_detector.detect_lanes(frame)

        dt = (time.clock()-t1)
        print("Approximate fps: "+str(1/dt))

        writer.write(output_img)

        cv2.imshow("Detected lanes", output_img)

    else:
        break

    # Press key q to stop
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
