from fastapi import FastAPI, Response, status, HTTPException,Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db, Base
from typing import Optional, List, Union
from .. import models , schemas, oauth2


router = APIRouter(
    prefix="/sqlalchemy",
    tags=["Posts"]
)


####################join with sqlalchemy#############################

@router.get("/")#, response_model=List[schemas.ResponsePost])
def get_join_posts(db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id,isouter = True).group_by(models.Post.id).all()
    
    return results
############################################################################










#test
# @router.get("/", response_model=List[schemas.ResponsePost])
# def test_post(db:Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
#                     limit: int = 5,skip: int=0, search:Optional[str] = ""):
    
#     print(limit)

#     posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()   
#     # posts = db.query(models.Post).all()
    
#     # if you want login user to see only his posts#
#     # posts = db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()

#     return posts

######################################

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponsePost)
def create_posts(post: schemas.PostCreate, db:Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # new_post = models.Post(title = post.title, content = post.content, 
    #             published= post.published)
    # print(current_user)
    new_post = models.Post(owner_id = current_user.id,**post.dict())


    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

######################################

@router.get("/{id}", response_model=schemas.ResponsePost)
def get_single_post(id : int, db:Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    fetched_post = db.query(models.Post).filter(models.Post.id == id).first()
    print(fetched_post)

    if not fetched_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} was not found")

    # if you want loginuser to see only his posts#
    # if fetched_post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")

    return fetched_post
    
######################################

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db:Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    Delete_post_query = db.query(models.Post).filter(models.Post.id == id)

    post = Delete_post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} was not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")

    Delete_post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

######################################

@router.put("/{id}", response_model=schemas.ResponsePost)
def update_post(id: int, updated_post: schemas.PostCreate, db:Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()
    

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id : {id} was not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")

    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit() 
    return post
