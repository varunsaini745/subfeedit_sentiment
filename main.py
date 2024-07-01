from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
from src import comment_sorting
from typing import Optional, Literal

app = FastAPI(title="Comment Classification", version="0.0.1")
prefix_router = APIRouter(prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@prefix_router.get("/")
async def health():
    return {"message": "Server running correctly"}


@prefix_router.get("/subfeddits")
async def get_data(url: str, subfeddit_id: int = 0,
                   skip: int = 0, limit: int = 25):
    response = requests.get(
        url, params={"subfeddit_id": subfeddit_id,
                     "skip": skip, "limit": limit}
    )
    return response.json()


@prefix_router.get("/subfeddits/comments")
async def get_sorting_data(
    url: str = "http://0.0.0.0:8080/api/v1/comments",
    polarity: Optional[Literal["asc", "desc"]] = None,
    subfeddit_id: int = 0,
    skip: int = 0,
    limit: int = 25,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
):
    final_response = comment_sorting(
        url=url,
        subfeddit_id=subfeddit_id,
        skip=skip,
        limit=limit,
        polarity=polarity,
        start_time=start_time,
        end_time=end_time,
    )
    return final_response


app.include_router(prefix_router)
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
