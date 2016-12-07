class Teacher(object):
    columns = ['id', 'create_time', 'name', 'age']
    table = 'teachers'

    def __init__(self, name, id=None, create_time=None, age=None):
        self.name = name
        self.id = id
        self.create_time = create_time
        self.age = age
