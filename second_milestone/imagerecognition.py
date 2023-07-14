import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    #print(frame)
    bbox, label_, conf = cv.detect_common_objects(frame)
    # print(label_)
    try:
        output_image = draw_bbox(frame, bbox, label_, conf)
    except ValueError as e:
        output_image = frame
        print(e)
    cv2.imshow('Object_Detection',output_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break





