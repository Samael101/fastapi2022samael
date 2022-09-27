from fastapi import FastAPI,Depends, APIRouter
from . import models
from .database import engine
from .routers import posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware
# models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# fetch('http://localhost:8000/').then(res=>res.json()).then(console.log)
###########################################################################################

# my_posts = [{"title" : "title of the post", "content" : "content of the post", "id" : 1},
#             {"title" : "favorite foods", "content" : "I like pizza", "id" : 2}]
################################ without sql ####################################################
@app.get("/")
def root():
    return {"message" : "Hello world  so far do good"}

################################ xxxxxxx ####################################################

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: schemas.PostCrete):
#     # print(post.rating)
#     post_dict = post.dict()
#     post_dict['id'] = randrange(0,1000000)
#     my_posts.append(post_dict)


# def retrieve_id(id):
#     return {"data" : my_posts}
#     for p in my_posts:
#         if p["id"] ==id:
#             return p

# @app.get("/posts/{id}")
# def get_single_post(id : int, response : Response):
#     post = retrieve_id(id)
#     if not post:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return{"message": f"post with id : {id} was not found"}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} was not found")
#     print(post)
#     return{"Post Detailed": {retrieve_id(id)}}

############################################################################################################################################

# def find_index(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     index = find_index(id)
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} was not found")


#     my_posts.pop(index)
#     return {"data": post_dict}

##################################################################

# @app.put("/posts/{id}")
# def update_post(id: int, post: schemas.PostCreate):
#     index = find_index(id)

#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"post with id : {id} was not found")

#     post_dict = post.dict()
#     post_dict['id'] = id
#     my_posts[index] = post_dict

#     return {"message": "updated post"}

############################################################################################
################################### with sql ###############################################
############################################################################################

# @app.get("/posts")
# def get_post():
#     cursor.execute("""Select * from posts""")
#     posts = cursor.fetchall()
#     print(posts)
#     return {"data" : posts}

# ##############################################

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: schemas.PostCreate):

#     cursor.execute("""
#                     INSERT INTO posts (title, content, published)
#                     VALUES (%s,%s,%s)
#                     RETURNING *""",(post.title, post.content, post.published)
#                     )
#     new_post = cursor.fetchone()
#     conn.commit()

#     return {"data" : new_post}

# ##############################################

# @app.get("/posts/{id}")
# def get_single_post(id : int, response : Response):
#     cursor.execute("""
#                     select * from posts where id=%s""", str(id))
#     fetched_post = cursor.fetchall()
#     conn.commit()
#     if not fetched_post:

#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} was not found")
#     print(fetched_post)
#     return{"Post Detailed": fetched_post}

# ##############################################

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     cursor.execute("""
#                     DELETE from posts where id=%s RETURNING *""", str(id))
#     Delete_post = cursor.fetchone()
#     conn.commit() 

#     if Delete_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} was not found")
#     print(Delete_post)
#     return {"data": Delete_post}

#     ##############################################

# @app.put("/posts/{id}")
# def update_post(id: int, post: schemas.PostCreate):
#     cursor.execute("""
#                     UPDATE posts SET title= %s, content= %s where id=%s RETURNING *""",
#                     (post.title, post.content, str(id)))
#     Updtd_post = cursor.fetchall()
#     conn.commit() 
#     if not Updtd_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"post with id : {id} was not found")

#     print(Updtd_post)
#     return {"message": Updtd_post}

############################################################################################
################################### sqlalchemy #############################################
############################################################################################
