from Print import Print
from Banner import Banner

class PrintBanner(Print):

    def __init__(self, strings):
        self.banner = Banner(strings)

    def printWeak(self):
        self.banner.showWithParen()

    def printStrong(self):
        self.banner.showWithAster()
