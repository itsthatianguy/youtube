from pydantic import BaseModel


class CreateJobRequest(BaseModel):
    title: str
    description: str
