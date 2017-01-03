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

    def __init__(self, name, id=None, create_time=None, age=None):
        self.name = name
        self.id = id
        self.create_time = create_time
        self.age = age


class Course(object):
    columns = ['id', 'create_time', 'code', 'department']
    table = 'courses'

    def __init__(self, code, department, id=None, create_time=None):
        self.id = id
        self.create_time = create_time
        self.code = code
        self.department = department


class StudentCourseMap(object):
    columns = ['id', 'create_time', 'student_id', 'course_id', 'grade']
    table = 'student_course_mapping'

    def __init__(self, student_id, course_id, grade, id=None, create_time=None):
        self.id = id
        self.create_time = create_time
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade


class TeacherCourseMap(object):
    columns = ['id', 'create_time', 'teacher_id', 'course_id']
    table = 'teacher_course_mapping'

    def __init__(self, teacher_id, course_id, id=None, create_time=None):
        self.id = id
        self.create_time = create_time
        self.teacher_id = teacher_id
        self.course_id = course_id
