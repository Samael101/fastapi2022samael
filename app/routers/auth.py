from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2


router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)


# def login(user_credential: schemas.UserLogin, db: Session = Depends(database.get_db)):

@router.post('/') # , response_model= schemas.Token | not working for me
def login(user_credential: OAuth2PasswordRequestForm= Depends(), db: Session = Depends(database.get_db)):
    
    user = db.query(models.User).filter(models.User.email==user_credential.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,  detail=f"Invalid Credentials")

    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create token
    # return token

    Access_Token = oauth2.create_access_token(data = {"user_id": user.id})

    return {"Access_Token": Access_Token, "Token_type": "bearer"}