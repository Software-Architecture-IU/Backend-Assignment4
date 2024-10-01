from sink import DisplaySink
from source import WebcamSource
from filters.dummy import DummyFilter
from filters.resize import ResizeFilter

from multiprocessing import Queue

dummyInput = Queue()
sinkInput = Queue()
resizeInput = Queue()

src = WebcamSource(outputs=[resizeInput])
dummy = DummyFilter(input=dummyInput, outputs=[sinkInput])
resize = ResizeFilter(input=resizeInput, outputs=[sinkInput], sizes=(800, 200))

sink = DisplaySink(input=sinkInput)

if __name__ == '__main__':
    src.start()
    dummy.start()
    resize.start()
    sink.start()

    sink.join()
    resize.join()
    dummy.join()
    src.join()