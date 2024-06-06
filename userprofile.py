class UserProfile:
    def __init__(self):
        self.server = ""
        self.user = ""
        self.webpage = ""
        self.date = None
        self.url = ""
        self.frequency = 0
        self.weight = 0
        self.pageDepth = 0

    def setServer(self, server):
        self.server = server

    def setUser(self, user):
        self.user = user

    def setWebpage(self, webpage):
        self.webpage = webpage

    def setDate(self, date):
        self.date = date

    def setURL(self, url):
        self.url = url

    def setFrequency(self, frequency):
        self.frequency = frequency

    def setWeight(self, weight):
        self.weight = weight

    def setPageDepth(self, pageDepth):
        self.pageDepth = pageDepth

    def getServer(self):
        return self.server

    def getUser(self):
        return self.user

    def getWebpage(self):
        return self.webpage

    def getDate(self):
        return self.date

    def getURL(self):
        return self.url

    def getFrequency(self):
        return self.frequency

    def getWeight(self):
        return self.weight

    def getPageDepth(self):
        return self.pageDepth
