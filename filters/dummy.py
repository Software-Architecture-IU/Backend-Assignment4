from filters.base import BaseFilter


class DummyFilter(BaseFilter):
    def process(self, frame):
        return frame
