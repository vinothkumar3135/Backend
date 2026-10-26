from pydantic import BaseModel, ConfigDict, Field


class BusinessCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    description: str = ""


class BusinessOut(BusinessCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    owner_id: int
