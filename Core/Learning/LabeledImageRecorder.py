import os
import shutil
import cv2
import numpy as np
from Components.Camera import Camera


class LabeledImageRecorder:
    # A class to sample and label camera frames for convnet training

    LABELS = np.array(["cube", "mug", "none"])
    TRAIN_DIR = "./data/train"
    VAL_DIR = "./data/validate"
    MAX_FRAMES = 1000

    def __init__(self, camera = Camera()):
        self.camera = camera

    def create_data_folders(self):
        if not os.path.exists(self.TRAIN_DIR):
            os.mkdir(self.TRAIN_DIR)
        if not os.path.exists(self.VAL_DIR):
            os.mkdir(self.VAL_DIR)

    def clean_image_data(self):

        for x in np.nditer(self.LABELS):
            os.mkdir(self.TRAIN_DIR + "/" + str(x))
            os.mkdir(self.VAL_DIR + "/" +  str(x))

    def record_image_data(self, directory, label):
        i = 1
        while(True):
            frame = self.camera.get_frame()
            frame = cv2.resize(frame, (150, 150), 0, 0)
            directory = directory

            if directory == self.TRAIN_DIR:
                cv2.imwrite(self.TRAIN_DIR + label + '/' + label + str(i) + '.png', frame)
            elif directory == self.VAL_DIR:
                cv2.imwrite(self.VAL_DIR + label + '/' + label + str(i) + '.png', frame)
            i = i + 1
            if i > self.MAX_FRAMES:
                break

if __name__ == '__main__':
    imagerecorder = LabeledImageRecorder()
    imagerecorder.create_data_folders()
    imagerecorder.record_image_data()