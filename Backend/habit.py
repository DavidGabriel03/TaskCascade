class Habit:
    def __init__(self, name, description, days):
        self.name = name
        self.description = description
        self.days = days

    def __str__(self):
        return f"{self.name} {self.description} {self.days}"

class HabitList:
    def __init__(self):
        self.habits = []
    def add_habit(self, habit):
        self.habits.append(habit)
    def remove_habit(self, habit):
        self.habits.remove(habit)
    def get_habits(self):
        return self.habits
    def get_habit_by_name(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None