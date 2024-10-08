from multiprocessing import Process, Queue

import cv2


class DisplaySink(Process):
    def __init__(self, input: Queue) -> None:
        super().__init__()
        self.input = input

    def run(self) -> None:
        while True:
            frame = self.input.get()
            if frame is None:
                break

            cv2.putText(frame, 'Press Q to Quit', (10, 30), cv2.QT_FONT_NORMAL, 0.95, (255, 255, 255), 3, cv2.LINE_AA)

            cv2.imshow('Processed Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
