from sink import DisplaySink
from source import WebcamSource
from filters.dummy import DummyFilter
from filters.mirror import MirrorFilter

from multiprocessing import Queue

dummyInput = Queue()
mirrorInput = Queue()
sinkInput = Queue()

src = WebcamSource(outputs=[dummyInput])
dummy = DummyFilter(input=dummyInput, outputs=[mirrorInput])
mirror = MirrorFilter(input=mirrorInput, outputs=[sinkInput])
sink = DisplaySink(input=sinkInput)

if __name__ == '__main__':
    src.start()
    dummy.start()
    mirror.start()
    sink.start()

    sink.join()
    dummy.join()
    mirror.join()
    src.join()