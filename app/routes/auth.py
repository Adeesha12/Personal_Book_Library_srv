from fastapi import APIRouter, HTTPException, Body, Depends
from typing import List, Optional
from model import BookItem, UserSchema, UserLoginSchema
from auth.jwt_handler import sign_jwt
from auth.jwt_bearer import JWTBearer



register_router = APIRouter(
    prefix="/v1/register",
    tags=["register"]
)

users = []
@register_router.post("/user/signup")
def user_signup(user:UserSchema = Body(default=None)) -> dict:
    users.append(user)
    return sign_jwt(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        else:
            return False

@register_router.post("/user/login")
def user_signup(user:UserLoginSchema = Body()) -> dict:
    if check_user(user):
        return sign_jwt(user.email)
    else:
        return {
            "error" : "invalid login details !"
        }
        