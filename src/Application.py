from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.authentication import auth_jwt
from src.controllers import authentication, user


class Application(FastAPI):
    def __init__(self):
        super().__init__(
            title=settings['API']['TITLE'],
            description=settings['API']['DESCRIPTION'],
            version=settings['API']['VERSION'],
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
