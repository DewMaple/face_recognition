import cv2

import face_recognition
import facerec_samples_reader as fr

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
# obama_image = face_recognition.load_image_file("obama.jpg")
# me_image = face_recognition.load_image_file("/Users/administrator/Documents/face_recognition/me.png")
# xiaozheng_image = face_recognition.load_image_file("/Users/administrator/Documents/face_recognition/xiaozheng.jpg")
# obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
# me_face_encoding = face_recognition.face_encodings(me_image)[0]
# xiaozheng_face_encoding = face_recognition.face_encodings(xiaozheng_image)[0]
image_encodings, names = fr.read("../data")

count = 0
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(image_encodings, face_encoding, tolerance=0.4)

        name = "Unknown"
        for i in range(0, len(match)):
            if match[i]:
                name = names[i]
                break

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    dynamic_part = "{0:08}".format(count)
    img_name = "{}/{}.jpg".format("recognized", dynamic_part)
    cv2.imwrite(img_name, frame)
    # Display the resulting image
    cv2.imshow('Video', frame)
    count += 1
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
