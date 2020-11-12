from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.authentication import auth_jwt
from src.controllers import authentication, user

class Application(FastAPI):
  def __init__(self):
    super().__init__()

  def boostrap(self):
    self.debug = settings['SERVER']['WSGI']['DEBUG']
    self.enableCors()
    self.configureCommonApis()
  
  def enableCors(self):
    self.add_middleware(
      CORSMiddleware,
      allow_credentials=True,
      allow_origins=["*"],
      allow_methods=["*"],
      allow_headers=["*"],
    )

  def configureCommonApis(self):
    self.include_router(authentication.router)
    self.include_router(user.router, dependencies=[Depends(auth_jwt)])
