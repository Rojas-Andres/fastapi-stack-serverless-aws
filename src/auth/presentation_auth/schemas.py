
from pydantic import BaseModel, EmailStr

class UserSignin(BaseModel):
    """
    Class for serializing the user signin.

    keys:
    - email: The user email.
    - password: The user password.
    """

    email: EmailStr
    password: str
