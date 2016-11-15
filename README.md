# Test Flask App
A lightweight Flask application used for teaching the basics of Python programming, APIs, and SQL. 
This repository is deliberately minified to keep teaching simple, it's purpose to to have the student expand
and build on top of it in tandem with my own additions and improvements to better simulate a Software Development workflow.

## Setup
```
pip install -r requirements.txt
```

## Usage
__Setting up database:__

Some SQL code has already been added to set up an initial schema of Teachers, Students, and Courses. 
This can be run to set up the SQLite database schema.
```
python db_setup.py
```

__Running Flask application:__
```
python app.py
```



# License
Copyright (c) 2016 Idrees Khan. See LICENSE file for full details.