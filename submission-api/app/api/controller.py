from fastapi import APIRouter
from .models import CreateSubmissionRequest
from . import db_manager

submissions = APIRouter()


@submissions.post('/', status_code=201)
async def create_submission(payload: CreateSubmissionRequest):
    submission_id = await db_manager.create_submission(payload)
    response = {
        'id': submission_id
    }

    return response
