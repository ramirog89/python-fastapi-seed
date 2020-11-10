from fastapi import APIRouter, Depends, HTTPException

from src.services.authentication import AuthenticationService
from src.schemas.login import LoginSchema
from src.schemas.token import TokenSchema

router = APIRouter()

@router.post('/auth/login', tags=['auth'], response_model=TokenSchema)
async def login(user: LoginSchema, service: AuthenticationService = Depends(AuthenticationService)):
  token = service.login(user.username, user.password)
  if not token:
    raise HTTPException(status_code=401, detail="Username or password invalid.")
  return { 'token': token }
