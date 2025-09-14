class Calendar:
    def __init__(self, year, month,day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"

    def __repr__(self):
        return f"<Calendar {self.year}/{self.month}/{self.day}>"
