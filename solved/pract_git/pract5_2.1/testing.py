class User:
    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role
    
    def authenticate(self, login_attempt, password_attempt):
        if self.login == login_attempt and self.password == password_attempt:
            return True
        else:
            return False
    
    def authorize(self, required_roles):
        if self.role in required_roles:
            return True
        else:
            return False


class Project:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        self.tasks.remove(task)
    
    def find_task_by_name(self, name):
        return [task for task in self.tasks if task.name == name]
    
    def find_task_by_start_date(self, start_date):
        return [task for task in self.tasks if task.start_date == start_date]
    
    def find_task_by_end_date(self, end_date):
        return [task for task in self.tasks if task.end_date == end_date]
    
    def is_completed(self):
        return all(task.status for task in self.tasks)
    
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'tasks': [task.to_dict() for task in self.tasks]
        }
    
    @classmethod
    def from_dict(cls, data):
        project = cls(data['name'], data['description'], data['start_date'], data['end_date'])
        for task_data in data['tasks']:
            task = Task.from_dict(task_data)
            project.add_task(task)
        return project


class Task:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = False
        self.performers = []
    
    def change_status(self):
        self.status = not self.status
    
    def add_performer(self, performer):
        self.performers.append(performer)
    
    def remove_performer(self, performer):
        self.performers.remove(performer)
    
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'status': self.status,
            'performers': self.performers
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data['name'], data['description'], data['start_date'], data['end_date'])
        task.status = data['status']
        task.performers = data['performers']
        return task


def test_objects():
    user = User(
        login="yunik",
        password="123321",
        role="student"
    )
    user.authenticate("yunik", "123321")
    user.authenticate("qwerty", "45678")

    user.authorize(["student"])
    user.authorize(["teacher"])
    
    task = Task()

    proj = Project(
        name="Gaembot",
        description="Game bot programm",
        start_date=10,
        end_date=15
    )
    proj.add_task("task1")
    proj.remove_task("task1")

    proj.find_task_by_name("task1")
    proj.find_task_by_start_date(10)
    proj.find_task_by_end_date(15)

    proj.is_completed()

    #proj.add_task("task2")
    dict_proj = proj.to_dict()
    proj = proj.from_dict(dict_proj)





