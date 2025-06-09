import contextlib

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 데이터베이스 URL 설정
SQLALCHEMY_DB_URL = "sqlite:///./myapi.db"

# SQLAlchemy 엔진 생성
engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={"check_same_thread":False}
)
# 세션 생성기 설정
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델 클래스의 기본 클래스 생성
Base = declarative_base()

#SQLite의 버그때문에 필요한 작업
naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base.metadata = MetaData(naming_convention=naming_convention)

# 데이터베이스 세션 객체를 생성하는 컨텍스트 매니저
# 데코레이터는 함수를 컨텍스트 매니저로 변환
# DB를 읽고 쓰는 작업에 atomicity를 보장
# @contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()