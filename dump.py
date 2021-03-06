#!/usr/bin/env python
"""
Dump Excel file to postgresql 'temp' database
"""

import os

import pandas as pd
from sqlalchemy import create_engine

import util
from runner import run

args = util.get_args()
INPUT_FILE = args.file or 'data.xlsx'
DB = args.db or 'temp'
TABLE = args.table or 'temp'


def main():
    # Connection params
    file = os.path.join(os.environ['USERPROFILE'],
                        'Desktop', 'Scripts', INPUT_FILE)
    user = os.environ['PGUSER']
    password = os.environ['PGPASSWORD']

    # dump
    df = pd.read_excel(file)
    engine = create_engine(
        f'postgresql://{user}:{password}@localhost:5432/{DB}')
    df.to_sql(TABLE, engine, if_exists='replace')


# -------------------MAIN----------------------#
if __name__ == '__main__':
    run(main)
