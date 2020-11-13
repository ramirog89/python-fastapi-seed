from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List

from src.authentication import SecurityRole
from src.services.businessLogic.user import UserBusinessLogicService, schema
from src.repositories.user import model
from src.schemas.pagination import PaginationSchema

router = APIRouter()

@router.get("/users", response_model=PaginationSchema[schema.User], tags=['users'])
def get(
  page: int = 0,
  limit: int = 10,
  sort: str = None,
  order: str = None,
  service: UserBusinessLogicService = Depends(),
  security: SecurityRole([model.UserRole.ADMIN.value]) = Depends()
):
  return service.getUserList(page, limit, sort, order)

@router.get("/users/{id}", response_model=schema.User, tags=['users'])
def get(
  id: str = None,
  service: UserBusinessLogicService = Depends(),
  security: SecurityRole([model.UserRole.ADMIN.value]) = Depends()
):
  try:
    return service.getById(id)
  except Exception as error:
    raise HTTPException(status_code=400, detail=str(error))

@router.post("/users", response_model=schema.User, tags=['users'])
def post(user: schema.UserCreate, service: UserBusinessLogicService = Depends()):
  try:
    return service.create(user)
  except Exception as error:
    raise HTTPException(status_code=400, detail=str(error))

@router.put("/users/{id}", response_model=schema.User, tags=['users'])
def update(id: int, user: schema.UserUpdate, service: UserBusinessLogicService = Depends()):
  try:
    return service.update(id, user)
  except Exception as error:
    raise HTTPException(status_code=400, detail=str(error))

@router.delete("/users/{id}", tags=['users'])
def delete(id: int, service: UserBusinessLogicService = Depends()):
  try:
    service.delete(id)
    return Response(status_code=status.HTTP_200_OK)
  except Exception as error:
    raise HTTPException(status_code=400, detail=str(error))
