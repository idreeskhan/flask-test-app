# Test Flask App
A lightweight Flask application used for teaching the basics of Python programming, APIs, and SQL. 
This repository is deliberately minified to keep teaching simple, it's purpose to to have the student expand
and build on top of it in tandem with my own additions and improvements to better simulate a Software Development workflow.

__The vast majority of this code is written by a student of mine learning to program in Python__

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

## Tasks

### Student Tasks
 - ~~Add models to `models.py` for all tables~~
 - Write out API spec based on examples in `api_routes.md`
 - Write out API routes in `app.py` using _flask_
   - Initially considering Updates to be out of scope for simplicity
 - Connect API routes to _sqlite_ database using `db.py`

### My Tasks
 - Initial database setup in `db_setup.py`
 - _Flask_ API route example
 - API spec example in `api_routes.md`
 - Generalized insert code
 - Generalized delete code
 - Basic HTML and JS webpage using routes provided in `app.py`
 
### Future Work
 - Supporting updating

# License
Copyright (c) 2016 Idrees Khan. See LICENSE file for full details.