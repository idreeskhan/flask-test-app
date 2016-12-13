# Students

## Retrieve All Students
GET     /api/students

## Retrieve One Student
GET     /api/students/?id=student_id

## Create A Student
POST    /api/students

__Body (Student as JSON):__
```
 {
    "id": null,
    "create_time": null,
    "name": "Idrees Khan",
    "age": 24
 }
```

## Update A Student
POST    /api/students
__Body (Student as JSON):__
```
 {
    "id": 1,
    "name": "Idrees Khan",
    "age": 240
 }
```