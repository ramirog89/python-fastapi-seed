from fastapi import APIRouter, Depends, HTTPException

from src.app.services.authentication import AuthenticationService
from src.app.schemas.login import LoginSchema
from src.app.schemas.token import TokenSchema

router = APIRouter()

@router.post('/auth/login', tags=['auth'], response_model=TokenSchema)
async def login(user: LoginSchema, service: AuthenticationService = Depends(AuthenticationService)):
  token = service.login(user.username, user.password)
  if not token:
    raise HTTPException(status_code=401, detail="Username or password invalid.")
  return { 'token': token }
