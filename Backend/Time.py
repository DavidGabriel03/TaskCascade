class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return "%02d:%02d" % (self.hour, self.minute)

    def showTimes(self):
        print(self)