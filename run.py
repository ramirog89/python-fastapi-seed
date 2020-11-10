import uvicorn

from src.config import settings

if __name__ == "__main__":
  uvicorn.run(
    "src:app",
    host=settings['SERVER']['WSGI']['HOSTNAME'],
    port=settings['SERVER']['WSGI']['PORT'],
    log_level=settings['SERVER']['WSGI']['LOG_LEVEL'],
    reload=settings['SERVER']['WSGI']['RELOAD']
  )
