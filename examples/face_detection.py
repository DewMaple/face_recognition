import argparse
import cv2
import face_recognition
import numpy as np

def detect(video_file, prefix):
    cap = cv2.VideoCapture(video_file)

    count = 0
    while cap.isOpened():
        ret, img = cap.read()

        # Bail out when the video file ends
        if not ret:
            break

        face_locations = face_recognition.face_locations(img=img)

        filename = _build_filename(count, prefix)
        print "{} face locations is {}".format(filename, face_locations)
        for face_location in face_locations:
            top, right, bottom, left = face_location
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow('detected', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.imwrite(filename, img)
        count += 1

    cap.release()


def _build_filename(count, prefix):
    dynamic_part = "{0:08}".format(count)
    return "{}_{}.jpg".format(prefix, dynamic_part)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('video_file', nargs='*')
    # parser.add_argument('-p', '--prefix', help='prefix of detected output image files')
    detect("/Users/administrator/Documents/video/quatum_students_0to2min.mp4", "quatum")
    # img = np.zeros((1000, 1000, 3), np.uint8)
    # cv2.rectangle(img, (784, 362), (828, 406), (0, 255, 0), 5)
    # cv2.imwrite("1111.jpg", img)
