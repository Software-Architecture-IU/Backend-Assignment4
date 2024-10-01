from multiprocessing import Process, Queue
from abc import ABC, abstractmethod
from typing import List

class BaseFilter(Process, ABC):
    def __init__(self, input: Queue, outputs: List[Queue]):
        super(BaseFilter, self).__init__()
        self.input = input
        self.outputs = outputs

    def run(self):
        while True:
            frame = self.input.get()
            processed = self.process(frame)
            for idx in range(len(self.outputs)):
                self.outputs[idx].put(processed)

    @abstractmethod
    def process(self, frame):
        pass
