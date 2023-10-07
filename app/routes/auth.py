from fastapi import APIRouter, Body
from model import  UserSchema, UserLoginSchema
from auth.jwt_handler import sign_jwt


register_router = APIRouter(
    prefix="/v1/register",
    tags=["register"]
)

users = []

@register_router.post("/user/signup")
def user_signup(user:UserSchema = Body(default=None)) -> dict:
    users.append(user)
    return sign_jwt(user.email)


@register_router.post("/user/login")
def user_signup(user:UserLoginSchema = Body()) -> dict:
    if check_user(user):
        return sign_jwt(user.email)
    else:
        return {
            "error" : "invalid login details !"
        }
        
        
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        else:
            return False