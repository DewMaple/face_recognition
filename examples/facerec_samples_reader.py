import glob
import os

import face_recognition as fr


def _load_image_encodings(images_dir):
    image_encodings = []
    print images_dir
    images_num = len(glob.glob1(images_dir, '*.jpg'))
    print images_num
    for i in range(0, images_num):
        dynamic_part = "{0:03}.jpg".format(i)
        image_name = "{}/{}".format(images_dir, dynamic_part)
        print image_name
        if os.path.isfile(image_name):
            img = fr.load_image_file(image_name)
            encoding = fr.face_encodings(img)[0]
            image_encodings.append(encoding)

    return image_encodings


def _load_names(names_file):
    names = []
    try:
        fp = open(names_file)
        line = fp.readline()
        while line:
            names.append(line.strip())
            line = fp.readline()
    finally:
        fp.close()

    print(names)
    return names


def read(dir_path="../data"):
    images_dir = os.path.join(dir_path, "images")
    img_encodings = _load_image_encodings(images_dir)
    names = _load_names(os.path.join(dir_path, 'names'))
    return img_encodings, names
