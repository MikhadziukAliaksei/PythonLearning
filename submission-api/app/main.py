from fastapi import FastAPI
from api import controller

app = FastAPI(openapi_url="/api/v1/submissions/openapi.json", docs_url="/api/v1/submissions/docs")

app.include_router(controller.submissions, prefix='/api/v1/submissions', tags=['submissions'])
