from pydantic import BaseModel

class FormDataBase(BaseModel):
    name: str
    age: int
    email: str
    company: str
    amount: int
    hospital: str
    county: str

class FormDataCreate(FormDataBase):
    pass

class FormData(FormDataBase):
    id: int

    class Config:
        orm_mode = True


