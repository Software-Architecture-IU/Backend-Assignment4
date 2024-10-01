from filters.base import BaseFilter
import cv2
class MirrorFilter(BaseFilter):
    def process(self, frame):
        new_frame = cv2.flip(frame, 1)
        return new_frame