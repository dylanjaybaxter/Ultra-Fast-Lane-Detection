import cv2

cap = cv2.VideoCapture("video0.avi")
if not cap.isOpened():
    print("Capture Failed")
    cap = None
w = int(cap.get(3))
h = int(cap.get(4))
size = (w,h)
writer = cv2.VideoWriter('./test.mp4',
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         20.0,
                         size)
while cap.isOpened():
    # Read frame from the video
    ret, frame = cap.read()

    if ret:
        writer.write(frame)

        cv2.imshow("Converted Video", frame)
    else:
        break

    # Press key q to stop
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()

