from multiprocessing import Queue

from filters.bnw import BnWFilter
from filters.dummy import DummyFilter
from filters.mirror import MirrorFilter
from filters.resize import ResizeFilter
from sink import DisplaySink
from source import WebcamSource

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

    src.kill()
    dummy.kill()
    resize.kill()
    mirror.kill()
    bnw.kill()
