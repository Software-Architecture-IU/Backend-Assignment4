from multiprocessing import Queue

from filters.bnw import BnWFilter
from filters.dummy import DummyFilter
from sink import DisplaySink
from source import WebcamSource

dummyInput = Queue()
sinkInput = Queue()

src = WebcamSource(outputs=[dummyInput])
dummy = DummyFilter(input=dummyInput, outputs=[sinkInput])
bnw = BnWFilter(input=dummyInput, outputs=[sinkInput])
sink = DisplaySink(input=sinkInput)

if __name__ == '__main__':
    src.start()
    dummy.start()
    bnw.start()
    sink.start()

    sink.join()
    dummy.join()
    bnw.join()
    src.join()
