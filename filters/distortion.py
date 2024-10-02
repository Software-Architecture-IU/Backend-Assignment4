from filters.base import BaseFilter

import cv2
import numpy as np


class DistortionFilter(BaseFilter):
    def process(self, frame):
        h, w = frame.shape[:2]
        k1 = -0.1
        k2 = -0.1

        x, y = np.meshgrid(np.linspace(-1, 1, w), np.linspace(-1, 1, h))
        r = np.sqrt(x ** 2 + y ** 2)
        x_distorted = x * (1 + k1 * r ** 2 + k2 * r ** 4)
        y_distorted = y * (1 + k1 * r ** 2 + k2 * r ** 4)

        map_x = ((x_distorted + 1) * w / 2).astype(np.float32)
        map_y = ((y_distorted + 1) * h / 2).astype(np.float32)

        distorted_img = cv2.remap(frame, map_x, map_y, interpolation=cv2.INTER_CUBIC)
        return distorted_img
