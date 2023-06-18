from pydantic import BaseModel
from typing import Optional


class CreateSubmissionRequest(BaseModel):
    admin_notes: Optional[str] = None

    class Track:
        name: str
        url: str
        artist_name: str
