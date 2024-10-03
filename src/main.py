from multiprocessing import Queue

from filters.bnw import BnWFilter
from filters.distortion import DistortionFilter
from filters.dummy import DummyFilter
from filters.mirror import MirrorFilter
from filters.resize import ResizeFilter
from sink import DisplaySink
from source import WebcamSource

dummyInput = Queue()
resizeInput = Queue()
mirrorInput = Queue()
bnwInput = Queue()
distortionInput = Queue()
sinkInput = Queue()

src = WebcamSource(outputs=[resizeInput])
dummy = DummyFilter(input=dummyInput, outputs=[resizeInput])
resize = ResizeFilter(input=resizeInput, outputs=[mirrorInput], sizes=(400, 400))
mirror = MirrorFilter(input=mirrorInput, outputs=[bnwInput])
bnw = BnWFilter(input=bnwInput, outputs=[distortionInput])
distort = DistortionFilter(input=distortionInput, outputs=[sinkInput], k1=-0.2, k2=0.5)
sink = DisplaySink(input=sinkInput)

processes = (src, dummy, resize, mirror, bnw, distort, sink)

if __name__ == '__main__':
    for process in processes:
        process.start()

    sink.join()

    for process in processes:
        process.kill()
