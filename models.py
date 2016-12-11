class Teacher(object):
    columns = ['id', 'create_time', 'name', 'age']
    table = 'teachers'

    def __init__(self, name, id=None, create_time=None, age=None):
        self.name = name
        self.id = id
        self.create_time = create_time
        self.age = age

class Student(object):
    columns = ['id', 'create_time', 'name', 'age']
    table = 'students'

    def __init__(self, name, id = None, create_time = None, age = None):
        self.name = name
        self.id = id
        self.create_time = create_time
        self.age = age

class Course(object):
    columns = ['id', 'create_time', 'code', 'department']
    table = courses

    def __init__(self, id = None, create_time = None, code, department):
        self.id = id
        self.create_time = create_time
        self.code = code
        self.department = department

class Student_Course_Map(object):
    columns = ['id', 'create_time', 'student_id', 'course_id', 'grade']
    table = 'student_course_mapping'

    def __init__(self, id = None, create_time = None, student_id, course_id, grade):
        self.id = id
        self.create_time = create_time
        slf.student_id = student_id
        self.course_id = course_id
        self.grade = grade

class Teacher_Course_Map(object):
    columns = ['id', 'create_time', 'teacher_id', 'course_id']
    table = 'teacher_course_mapping'

    def __init__(self, id = None, create_time = None, teacher_id, course_id, grade):
        self.id = id
        self.create_time = create_time
        self.teacher_id = teacher_id
        self.course_id = course_id
        
