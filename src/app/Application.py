from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from src.app.config import settings
from src.app.authentication import auth_jwt
from src.app.controllers import authentication, user

class Application(FastAPI):
  settings = None

  def __init__(self):
    super().__init__(
      docs_url=settings['SWAGGER']['DOCS_URL'],
      redoc_url=settings['SWAGGER']['REDOC_URL']
    )

  def boostrap(self):
    self.debug = settings['SERVER']['DEBUG']
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
