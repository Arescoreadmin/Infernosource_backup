from pydantic import BaseModel

class PageOut(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
