from multiprocessing import Process, Queue
from typing import List

import cv2


class WebcamSource(Process):
    def __init__(self, outputs: List[Queue]) -> None:
        super().__init__()
        self.outputs = outputs

    def run(self) -> None:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            for idx in range(len(self.outputs)):
                self.outputs[idx].put(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
