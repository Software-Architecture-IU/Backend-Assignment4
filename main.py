from sink import DisplaySink
from source import WebcamSource
from filters.dummy import DummyFilter

from multiprocessing import Queue

dummyInput = Queue()
sinkInput = Queue()

src = WebcamSource(outputs=[dummyInput])
dummy = DummyFilter(input=dummyInput, outputs=[sinkInput])
sink = DisplaySink(input=sinkInput)

if __name__ == '__main__':
    src.start()
    dummy.start()
    sink.start()

    sink.join()
    dummy.join()
    src.join()