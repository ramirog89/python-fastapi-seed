import uvicorn

from src.app.config import settings

if __name__ == "__main__":
  uvicorn.run(
    "src.app:app",
    host=settings['SERVER']['HOSTNAME'],
    port=settings['SERVER']['PORT'],
    log_level=settings['SERVER']['LOG_LEVEL'],
    reload=settings['SERVER']['RELOAD']
  )
