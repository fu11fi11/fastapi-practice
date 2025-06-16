# FastAPI Practice Project([점프 투 FastAPI](https://wikidocs.net/book/8531))

이 프로젝트는 FastAPI를 사용한 백엔드와 Svelte를 사용한 프론트엔드로 구성된 풀스택 웹 애플리케이션입니다.  

## 프로젝트 구조

```
fastapi-practice/
├── frontend/           # Svelte 프론트엔드
├── domain/            # 도메인 로직
├── migrations/        # Alembic 데이터베이스 마이그레이션
├── logs/             # 로그 파일
├── main.py           # FastAPI 메인 애플리케이션
├── database.py       # 데이터베이스 설정
├── models.py         # SQLAlchemy 모델
├── requirements.txt  # Python 의존성
└── package.json      # Node.js 의존성
```

## 기술 스택

### 백엔드
- FastAPI
- SQLAlchemy (ORM)
- Alembic (데이터베이스 마이그레이션)
- SQLite (데이터베이스)
- Python 3.x

### 프론트엔드
- Svelte
- Vite
- Node.js

## 시작하기

### 백엔드 설정

1. Python 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 데이터베이스 마이그레이션
```bash
alembic upgrade head
```

4. 서버 실행
```bash
uvicorn main:app --reload
```

### 프론트엔드 설정

1. 프론트엔드 디렉토리로 이동
```bash
cd frontend
```

2. 의존성 설치
```bash
npm install
```

3. 개발 서버 실행
```bash
npm run dev
```

4. 프로덕션 빌드
```bash
npm run build
```

## API 엔드포인트

- `/` - 메인 페이지
- `/assets` - 정적 파일 서빙
- 기타 API 엔드포인트는 domain 디렉토리의 라우터에서 확인할 수 있습니다.

## 환경 설정

- 백엔드 서버는 기본적으로 `http://localhost:8000`에서 실행됩니다.
- 프론트엔드 개발 서버는 기본적으로 `http://localhost:5173`에서 실행됩니다.
- CORS 설정이 되어 있어 로컬 개발 환경에서 프론트엔드와 백엔드 간의 통신이 가능합니다.

## 로깅

- 로그 파일은 `logs` 디렉토리에 저장됩니다.
- 기본 로깅 레벨은 DEBUG로 설정되어 있습니다. 
