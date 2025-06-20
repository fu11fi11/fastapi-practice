from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
import logging

from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
origins = [
        "http://localhost:5173",
        "http://localhost:8000",
        "http://localhost:8000/",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8000/",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#     return {"message":"안녕하세요 파이보"}

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))

@app.get("/")
def index():
    logger.debug("Root path requested")
    try:
        return FileResponse("frontend/dist/index.html")
    except Exception as e:
        logger.error(f"Error serving index.html: {str(e)}")
        raise