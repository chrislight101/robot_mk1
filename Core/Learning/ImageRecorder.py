import numpy as np
import cv2
import os
import shutil
import time
from Core.Vision.Camera import Camera


class ImageRecorder:
    # A class to sample and label camera frames for convnet training

    LABELS = np.array(["cube", "mug", "none"])
    TRAIN_DIR = "./data/train"
    VAL_DIR = "./data/validate"

    def __init__(self, camera = None):
        self.camera = camera

    def clean_image_data(self):
        if os.path.exists(self.TRAIN_DIR):
            shutil.rmtree(self.TRAIN_DIR)
        os.mkdir(self.TRAIN_DIR)
        if os.path.exists(self.VAL_DIR):
            shutil.rmtree(self.VAL_DIR)
        os.mkdir(self.VAL_DIR)

        for x in np.nditer(self.LABELS):
            os.mkdir(self.TRAIN_DIR + "/" + str(x))
            os.mkdir(self.VAL_DIR + "/" +  str(x))

    def record_image_data(self):
        self.camera.open_capture()
        while(True):
            frame = self.camera.get_frame()
            frame = cv2.resize(frame, (150, 150), 0, 0)

            if writetraindata:
                cv2.imwrite('./data/train/' + imlbl + '/' + imlbl + str(i) + '.png', frame)
            else:
                cv2.imwrite('./data/validation/' + imlbl + '/' + imlbl + str(i) + '.png', frame)
            i = i + 1
            if i >= max_i:
                writeimgfiles = False
                status = "REC_OFF"
                i = 0
