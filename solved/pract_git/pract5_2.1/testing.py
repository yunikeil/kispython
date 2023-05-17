import datetime

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
    user = User("yunikeil", "123321", "student")

    assert user.authenticate("yunikeil", "123321") == True
    assert user.authenticate("yunikeil", "321123") == False

    assert user.authorize("student") == True
    assert user.authorize("stuudent") == False

    project = Project("user project", "projdesc", "24.06.2021", "24.12.2021")

    task1 = Task("task1", "task1desc", "10.07.2021", "28.08.2021")
    task2 = Task("task2", "task2desc", "19.12.2021", "24.12.2021")

    task1.change_status()
    assert task1.status == True

    task1.add_performer("yunikeil")
    assert task1.performers == ["yunikeil"]

    task1.remove_performer("yunikeil")

    assert task1.performers == []
    assert task1.to_dict() == {
        'name': "task1",
        'description': "task1desc",
        'start_date': "10.07.2021",
        'end_date': "28.08.2021",
        'status': True,
        'performers': []
    }
    x = task1.to_dict()
    assert task1.from_dict(x)

    project.add_task(task1)
    project.add_task(task2)

    assert project.find_task_by_name("task1")
    assert project.find_task_by_name("task2")

    assert project.find_task_by_start_date('10.07.2021')
    assert project.find_task_by_end_date('28.08.2021')

    dict = project.to_dict()
    assert project.from_dict(dict)
    
    project.remove_task(task2)
    assert project.is_completed()


