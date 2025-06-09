#라우팅 = URL 해석 + 함수 실행 + 결과 리턴
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db
# from models import Question
from domain.question import question_schema, question_crud
from domain.user.user_router import get_current_user
from models import User

router = APIRouter(
    prefix="/api/question",
)

#fastapi에게 question_list함수가 /api/question/list 경로로의 get하는 함수임을 알리는 데코레이터
#response model파라미터를 통해 question_list 함수의 리턴값은 question schema로 구성되었음을 알림
@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db),
                    page: int = 0, size:int=10,
                    keyword:str=''):
    # 방법1
    # db = SessionLocal()
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    # db.close()
    # return _question_list
    
    # 방법2
    # with get_db() as db:
    #     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    #     return _question_list

    #방법3(인자로 db:Session = Depends(get_db) 넣어줘야 가능)
    #depends는 매개변수로 전달받음 함수 호출한 뒤 결과 리턴
    # _question_list = question_crud.get_question_list(db)
    # return _question_list

    total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size, keyword=keyword)
    
    return {
        'total': total,
        'question_list': _question_list
    }
    
@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
    db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):

    question_crud.create_question(db=db, 
    question_create=_question_create,
    user=current_user)

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def question_update(_question_update:question_schema.QuestionUpdate,
            db:Session=Depends(get_db),
            current_user: User=Depends(get_current_user)):
    
    db_question = question_crud.get_question(db, question_id=_question_update.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    question_crud.update_question(db_question=db_question, db=db, question_update=_question_update)

@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def question_delete(_question_delete:question_schema.QuestionDelete,
            db:Session=Depends(get_db),
            current_user: User=Depends(get_current_user)):

    db_question = question_crud.get_question(db, question_id=_question_delete.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    
    question_crud.delete_question(db_question=db_question, db=db)