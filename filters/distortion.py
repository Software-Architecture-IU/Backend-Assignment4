from filters.base import BaseFilter

import cv2
import numpy as np

from typing import List
from multiprocessing import Queue


class DistortionFilter(BaseFilter):
    def __init__(self, input: Queue, outputs: List[Queue], k1: float, k2: float):
        super(DistortionFilter, self).__init__(input=input, outputs=outputs)
        self.k1 = k1
        self.k2 = k2

    def process(self, frame):
        h, w = frame.shape[:2]

        x, y = np.meshgrid(np.linspace(-1, 1, w), np.linspace(-1, 1, h))
        r = np.sqrt(x ** 2 + y ** 2)
        x_distorted = x * (1 + self.k1 * r ** 2 + self.k2 * r ** 4)
        y_distorted = y * (1 + self.k1 * r ** 2 + self.k2 * r ** 4)

        map_x = ((x_distorted + 1) * w / 2).astype(np.float32)
        map_y = ((y_distorted + 1) * h / 2).astype(np.float32)

        distorted_img = cv2.remap(frame, map_x, map_y, interpolation=cv2.INTER_CUBIC)
        return distorted_img
