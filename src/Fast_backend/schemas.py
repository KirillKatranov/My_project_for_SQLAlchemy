from pydantic import BaseModel, Field


class GetContentSchemas(BaseModel):
    link: str = Field(le=500)
    topic: str = Field(le=500)
    source: str = Field(le=500)