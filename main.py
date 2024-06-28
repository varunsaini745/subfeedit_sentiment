from fastapi import FastAPI, HTTPException, APIRouter, status, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
from src import comment_sentiment, comment_sorting


app = FastAPI(title = "Comment Classification", version = "0.0.1")
prefix_router = APIRouter(prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@prefix_router.get("/")
async def root():
    return {"message": "Server running correctly"}

@prefix_router.get("/subfeddits")
async def get_data(url:str, subfeddit_id: int = 0, skip: int =  0, limit: int = 25):
    response = requests.get(url, params={"subfeddit_id": subfeddit_id, "skip": skip, "limit": limit})
    return response.json()

@prefix_router.post("/subfeddits/commentSentiment")
async def post_sentiment_data(url: str= "http://0.0.0.0:8080/api/v1/comments", subfeddit_id: int = 0, skip: int =  0, limit: int = 25):
    final_response = comment_sentiment(url, subfeddit_id, skip, limit)
    return final_response

@prefix_router.post("/subfeddits/commentsorting")
async def post_sorting_data(url: str= "http://0.0.0.0:8080/api/v1/comments", sorting_parameter: str = "polarity", subfeddit_id: int = 0, skip: int =  0, limit: int = 25, start_time: int = 0, end_time: int = 0):
    final_response = comment_sorting(url, sorting_parameter, subfeddit_id, skip, limit, start_time, end_time)
    return final_response


app.include_router(prefix_router)
if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)