from multiprocessing import Queue
from typing import List, Tuple

import cv2

from filters.base import BaseFilter


class ResizeFilter(BaseFilter):
    def __init__(self, input: Queue, outputs: List[Queue], sizes: Tuple[int, int]):
        super(ResizeFilter, self).__init__(input, outputs)
        self.sizes = sizes

    def run(self):
        return super().run()

    def process(self, frame):
        return cv2.resize(frame, self.sizes)
