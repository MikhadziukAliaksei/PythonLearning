from sqlalchemy import (Column, DateTime, Integer, String, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Submission(Base):
    __tablename__ = 'submission'
    id = Column(Integer, primary_key=True)
    admin_notes = Column(String)
    created_on = Column(DateTime)
    track = relationship("Track", back_populates="submission", uselist=False)


class Track(Base):
    __tablename__ = 'track'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    artist_name = Column(String)
    submission_id = Column(Integer, ForeignKey('submission_id'))
    submission = relationship("Submission", back_populates="track")

