import sys
import cv2

# Open the default camera
cam_index = 0
if len(sys.argv) == 2:
    cam_index = int(sys.argv[1])

cam = cv2.VideoCapture(cam_index)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam.get(cv2.CAP_PROP_FPS))

print("camera:", cam_index, "frame_width:", frame_width, "frame_height:", frame_height, "fps:", fps)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    # Write the frame to the output file
    out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera: ' + str(cam_index), frame)

    # Press 'q' to exit the loop
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()

