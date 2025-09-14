class Task:
    def __init__(self, id,name, description, status, start_time, end_time):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.start_time = start_time
        self.end_time = end_time

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_start_time(self):
        return self.start_time
    def get_end_time(self):
        return self.end_time
    def get_id(self):
        return self.id
    def set_name(self,name):
        self.name=name;
    def set_description(self,description):
        self.description=description;
    def set_status(self,status):
        self.status=status;
    def set_start_time(self,start_time):
        self.start_time=start_time;
    def set_end_time(self,end_time):
        self.end_time=end_time;
    def __repr__(self):
        return f"<Task {self.name} {self.description} {self.status} {self.start_time} {self.end_time}>"

    def __str__(self):
        return f"{self.name} {self.description} {self.status} {self.start_time} {self.end_time}"
import json

class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, task):
        self.tasks.remove(task)
    def get_tasks(self):
        for task in self.tasks:
            yield task
    def editTaskbyName(self,id,name):
        self.tasks[id].name=name;
    def editTaskbyDescription(self,id,description):
        self.tasks[id].description=description;
    def editTaskbyStatus(self,id,status):
        self.tasks[id].status=status;
    def editTaskbyStartTime(self,id,start_time):
        self.tasks[id].start_time=start_time;
    def editTaskbyEndTime(self,id,end_time):
        self.tasks[id].end_time=end_time;
    def get_task_by_name(self, name):
        for task in self.tasks:
            if task.name == name:
                return task
    def get_task_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
    def get_task_by_description(self, description):
        for task in self.tasks:
            if task.description == description:
                return task
    def get_task_by_status(self, status):
        for task in self.tasks:
            if task.status == status:
                return task
    def get_task_by_start_time(self, start_time):
        for task in self.tasks:
            if task.start_time == start_time:
                return task
    def get_task_by_end_time(self, end_time):
        for task in self.tasks:
            if task.end_time == end_time:
                return task
    # ------------------ JSON RELATED --------------------
    def save_to_json(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump([task.__dict__ for task in self.tasks], f, indent=4)

    def load_from_json(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**item) for item in data]
        except FileNotFoundError:
            self.tasks = []


