from pydantic import BaseModel

class ExtensionCreate(BaseModel):
    name: str
    description: str

class ExtensionOut(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True