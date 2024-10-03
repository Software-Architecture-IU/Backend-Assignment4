import cv2

from src.filters.base import BaseFilter


class BnWFilter(BaseFilter):
    def process(self, frame):
        new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return new_frame
