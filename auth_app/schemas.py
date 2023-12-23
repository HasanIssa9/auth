from ninja import Schema
from pydantic import EmailStr, Field


class FourOFourOut(Schema):
    detail: str

class AccountIn(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    password1: str = Field(min_length=8)
    password2: str = Field(min_length=8)


class TokenOut(Schema):
    access: str


class AccountOut(Schema):
    first_name: str
    last_name: str
    email: EmailStr


class AuthOut(Schema):
    token: TokenOut
    account: AccountOut


class SigninIn(Schema):
    email: EmailStr
    password: str = Field(min_length=8)

class LogOut(Schema):
    detail: str