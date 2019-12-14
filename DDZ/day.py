from lecture import Lecture


class Day:
    def __init__(self):
        self.lectures = [None] * 4

    def addlecture(self, lecture):
        self.lectures.append(lecture)
