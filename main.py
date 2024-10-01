from sink import DisplaySink
from source import WebcamSource
from filters.dummy import DummyFilter
from filters.resize import ResizeFilter
from filters.mirror import MirrorFilter
from filters.bnw import BnWFilter

from multiprocessing import Queue

dummyInput = Queue()
resizeInput = Queue()
mirrorInput = Queue()
bnwInput = Queue()
sinkInput = Queue()

src = WebcamSource(outputs=[resizeInput])
dummy = DummyFilter(input=dummyInput, outputs=[resizeInput])
resize = ResizeFilter(input=resizeInput, outputs=[mirrorInput], sizes=(800, 200))
mirror = MirrorFilter(input=mirrorInput, outputs=[bnwInput])
bnw = BnWFilter(input=bnwInput, outputs=[sinkInput])
sink = DisplaySink(input=sinkInput)

if __name__ == '__main__':
    src.start()
    dummy.start()
    resize.start()
    mirror.start()
    bnw.start()
    sink.start()

    sink.join()
    bnw.join()
    mirror.join()
    resize.join()
    dummy.join()
    src.join()
