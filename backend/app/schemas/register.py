from pydantic import BaseModel
class UserDetails(BaseModel): 
    Name:str
    email:str
    password_hash:str
    education_level:str
    years_of_experience:int
    career_interest:str


class LoginDetails(BaseModel):
    email:str
    password_hash:str