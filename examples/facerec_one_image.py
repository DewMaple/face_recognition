import sys

import cv2

import face_recognition

# args = sys.argv
#
# if len(args) < 4:
#     print 'You should set a sample image and an image to be recognized, for example, ' \
#           './facerec_one_image.py sample.jpg sample test.jpg'
#     exit(-1)
# print args
# sample_img = args[1]
# sample_name = args[2]
# test_img = args[3]
sample_img = "/Users/administrator/Downloads/Gal_Gadot.jpg"
sample_name = "Gal Gadot"
test_img = "/Users/administrator/Downloads/Gal_Gadot_03.jpg"
sample_image = face_recognition.load_image_file(sample_img)

sample_face_encoding = face_recognition.face_encodings(sample_image)[0]
print 'type a is {}'.format(type(sample_face_encoding))
frame = cv2.imread(test_img)
face_locations = face_recognition.face_locations(frame)
face_encodings = face_recognition.face_encodings(frame, face_locations)

sample_fes = [sample_face_encoding]
print 'type of sample fes is {}'.format(type(sample_fes))
print sample_fes
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    print 'type of face_encoding is {}'.format(type(face_encoding))
    print face_encoding
    match = face_recognition.compare_faces(sample_fes, face_encoding, tolerance=0.6)

    name = "Unknown"
    for i in range(0, len(match)):
        if match[0]:
            name = sample_name
            break

    # Draw a box around the face
    cv2.rectangle(frame, (left, top), (right, bottom), (250, 255, 18), 2)

    # Draw a label with a name below the face
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (250, 255, 18), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (252, 116, 39, 1), 1)

img_name = "{}/{}.jpg".format("recognized", "Gal Gadot-03")
cv2.imwrite(img_name, frame)
cv2.imshow('Video', frame)

cv2.destroyAllWindows()
