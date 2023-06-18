import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

submissions = Table(
    'submissions',
    metadata,
    Column('id', int, primary_key=True),
    Column('admin_notes', String),
    Column('CreatedOn', DateTime)
)

tracks = Table(
    'tracks',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('submission_id', Integer),
    Column('name', String),
    Column('url', String),
    Column('artist_name', String)
)

databases = Database(DATABASE_URI)
