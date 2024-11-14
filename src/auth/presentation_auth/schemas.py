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


class UserCreate(BaseModel):
    """
    Class for serializing the user creation.

    keys:
    - email: The user email.
    - password: The user password.
    - first_name: The user first name.
    - last_name: The user last name.
    """

    username: str
    email: EmailStr
    password: str
    first_name: str
    address: str
    phone: str
