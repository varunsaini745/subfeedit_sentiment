from src.comment_sentiment import comment_sentiment
from typing import Optional


def comment_sorting(
    url: str,
    subfeddit_id: int = 0,
    skip: int = 0,
    limit: int = 25,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
    polarity: Optional[str] = None,
):
    final_result = comment_sentiment(url, subfeddit_id, skip, limit)
    if start_time is not None and end_time is not None:
        # Filter comments by a specific time range
        final_result = [
            comment
            for comment in final_result
            if (comment["created_time"] >= start_time)
            and (comment["created_time"] <= end_time)
        ]
    if polarity == "asc":
        final_result = sorted(final_result, key=lambda x: x["polarity"], reverse=False)
    elif polarity == "desc":
        final_result = sorted(final_result, key=lambda x: x["polarity"], reverse=True)
    return final_result
