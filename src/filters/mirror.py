import cv2

from src.filters.base import BaseFilter


class MirrorFilter(BaseFilter):
    def process(self, frame):
        new_frame = cv2.flip(frame, 1)
        return new_frame
