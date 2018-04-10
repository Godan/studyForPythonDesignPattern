from Banner import Banner

class PrintBanner(Banner):

    def __init__(self, strings):
        self.banner = Banner(strings)

    def printWeak(self):
        self.banner.showWithParen()

    def printStrong(self):
        self.banner.showWithAster()
