import sqlite3
import logging
from models import Teacher


def insert_teacher(teacher):
    with sqlite3.connect('my-app.db') as conn:
        logging.debug('Inserting teacher {}'.format(teacher))
        input_cols = [col for col in Teacher.columns if getattr(teacher, col) is not None]
        vals = [getattr(teacher, col) for col in input_cols]
        query_params = '(' + ','.join(['?'] * len(input_cols)) + ')'
        q = """
            INSERT INTO {} (name) VALUES {}
        """.format(Teacher.table, input_cols, query_params)
        print('Running query {}'.format(q))
        conn.execute(q, vals)
