from database import Session
from db import Submission, Track
from models import CreateSubmissionRequest


def create_submission(payload: CreateSubmissionRequest):
    session = Session()
    track = Track(
        name=CreateSubmissionRequest.Track.name,
        url=CreateSubmissionRequest.Track.url,
        artist_name=CreateSubmissionRequest.Track.artist_name)
    submission = Submission(admin_notes=CreateSubmissionRequest.admin_notes, track=track)
    session.add(submission)
    session.commit()
    session.close()
    return submission.id


def read_submission(id):
    session = Session()
    submission = session.query(Submission).filter(Submission.id == id).first()
    session.close()
    return submission


def delete_submission(id):
    session = Session()
    submission = session.query(Submission).filter(Submission.id == id).first()
    if submission is not None:
        session.delete(submission)
        session.commit()
    session.close()
