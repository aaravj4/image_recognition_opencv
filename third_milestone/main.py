import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import html

flag = 0
video = cv2.VideoCapture(0)
sender = "jainaarav100@outlook.com"
recipient = "jainaarav100@outlook.com"
password = "SCkd304!!"

def email_new(subject, msg, image):
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient
    
    # Attach the message as plain text
    msg_text = MIMEText(msg, "plain")
    message.attach(msg_text)

    # Attach the image
    img_data = open(image, 'rb').read()
    image_mime = MIMEImage(img_data, name='image.jpg')
    message.attach(image_mime)
    
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, message.as_string())

while True:
    ret, frame = video.read()
    bbox, label_, conf = cv.detect_common_objects(frame)

    try:
        output_image = draw_bbox(frame, bbox, label_, conf)
    except ValueError as e:
        output_image = frame
        print(e)

    cv2.imshow('Object_Detection', output_image)
    
    if flag == 0 and 'person' in label_:
        print('Person detected!')
        
        # Save the image with bounding boxes
        image_path = 'detected_image.jpg'
        cv2.imwrite(image_path, output_image)

        # Send email with image attachment
        email_subject = "A person was detected outside your house"
        email_message = "A person was detected in your camera"
        email_new(email_subject, email_message, image_path)
        
        flag = 1

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

